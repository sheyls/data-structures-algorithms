"""
Problem Statement:

Design and implement a system that processes a stream of loans in real time. Each loan has an associated volume, and the system must support the following two operations:

store_loan(volume):
Persist (store) a loan’s volume at the time it is received.

get_loan_volume():
Return a summary (e.g., the total sum) of the loan volumes that were recorded in the last hour (i.e., the past 3600 seconds).

Requirements:

Implementation Language:
You may choose any programming language.

Initial Implementation:
You are not required to optimize for time or space initially. However, you must describe the time and space complexity of each function (store_loan and get_loan_volume) after your implementation.

Follow-Up:
Propose an alternative solution that achieves constant space complexity (O(1)) for storing and processing the loans, even if that means the returned result may be approximate (i.e., not fully accurate).
"""

from typing import Dict
from time import time

DELIMITER_TIME = 3600 #sec

class LoanAggregator:

    def __init__(self):
        self.loans: Dict[float, int] = {} #Hashmap from timestamp to volume

    def store_loan(self, volume: int) -> None:
        current_time = time()     
        self.loans[current_time] = volume

    def get_loan_volume(self) -> int:
        current_time = time()
        allowed_time = current_time - DELIMITER_TIME
        total = sum([v for k,v in self.loans.items() if k >= allowed_time and k < current_time])
        return total
    
# Time Complexity: O(N)
# Space Complexity: O(N)

# Sol 2

class LoanAggregatorApprox:
    def __init__(self, num_buckets: int = 60):
        self.num_buckets = num_buckets
        # Cada bucket cubre un intervalo de 3600 / num_buckets segundos
        self.bucket_duration = 3600 // num_buckets
        # Inicializamos la lista de buckets: cada bucket es un par (bucket_start_time, aggregated_volume)
        self.buckets = [(0, 0) for _ in range(num_buckets)]
    
    def store_loan(self, volume: int) -> None:
        current_time = int(time.time())
        bucket_index = (current_time // self.bucket_duration) % self.num_buckets
        bucket_start = (current_time // self.bucket_duration) * self.bucket_duration
        
        bucket_time, bucket_volume = self.buckets[bucket_index]
        if bucket_time != bucket_start:
            # El bucket es viejo; reinicializarlo
            self.buckets[bucket_index] = (bucket_start, volume)
        else:
            # Actualizar el bucket con el nuevo volumen
            self.buckets[bucket_index] = (bucket_time, bucket_volume + volume)
    
    def get_loan_volume(self) -> int:
        current_time = int(time.time())
        total = 0
        # Sumamos solo los bucketsque están dentro de la ventana de 3600 segundos
        for bucket_time, bucket_volume in self.buckets:
            if current_time - bucket_time < 3600:
                total += bucket_volume
        return total


# Example
loan_aggregator = LoanAggregator()
loan_aggregator.store_loan(100)
loan_aggregator.store_loan(200)
loan_aggregator.store_loan(300)
print(loan_aggregator.get_loan_volume()) # 600
loan_aggregator.store_loan(400)
loan_aggregator.store_loan(500)
print(loan_aggregator.get_loan_volume()) # 1500
