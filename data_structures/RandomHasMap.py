"""
Implement a custom HashMap that supports the following operations:

put(String key, int value):
Insert a key-value pair into the map.
Note: A key may be inserted multiple times with different values.
Challenge: New values for an existing key must be handled correctly.

delete(String key):
Remove a key (and its associated value) from the map.
Initial time complexity requirement: O(n).

get(String key):
Retrieve the value(s) associated with a given key.
Initial time complexity requirement: O(n).

findRandom():
Return a random value from the current map such that each value is chosen with a probability proportional to its frequency (i.e., duplicate values are more likely to be picked).
Time complexity requirement: O(1).

Additional Details:

The data structure must allow duplicate values. That is, different keys might map to the same value, and the same key can be inserted multiple times with different values.
The underlying storage for values should conceptually be an ArrayList of pairs (e.g., Pair<String, int>), so that findRandom() can operate in O(1) time.
The probability in findRandom() should reflect the frequency of values. For example, if the map contains:
A -> 1
B -> 1
C -> 2
then the probability of selecting the value 1 should be 1/2 and that of 2 should be 1/2 (as opposed to a scenario where the probability is weighted by frequency, e.g., 1 being selected 2/3 of the time).

Follow-up Questions:
Probability Independence:
How would you modify your design so that the probability of a value being selected by findRandom() is independent of its frequency? In other words, if the map has:
A -> 1
B -> 1
C -> 2
the selection probability should be 1/2 for 1 and 1/2 for 2, not weighted by the count of occurrences.
Optimizing put():
How can you optimize your put() operation to run in O(1) time?
Hint: Using an ArrayList of Pair<String, int> (or equivalent) for storage may simplify achieving O(1) insertion.
"""

import random
from collections import defaultdict

class RandomizedHashMap:
    def __init__(self):
        self.data = []  
        # Diccionario: key -> set of indices in self.data
        self.idx_map = defaultdict(set)
    
    def put(self, key: str, value: int) -> None:
        """
        Insert a new (key, value) pair.
        Duplicate keys are allowed: each put inserts a new pair.
        Time: O(1) on average.
        """
        self.data.append((key, value))
        self.idx_map[key].add(len(self.data) - 1)
    
    def get(self, key: str) -> list:
        """
        Retrieve all values associated with key.
        Time: O(k) where k is the number of occurrences of key.
        """
        return [self.data[i][1] for i in self.idx_map.get(key, [])]
    
    def delete(self, key: str) -> bool:
        """
        Delete one occurrence of the key.
        Time: O(1) on average.
        """
        if key not in self.idx_map or not self.idx_map[key]:
            return False
        
        # Get an arbitrary index for the key
        remove_idx = self.idx_map[key].pop()
        last_idx = len(self.data) - 1
        
        # If the element to remove is not the last one, swap with the last element.
        if remove_idx != last_idx:
            last_pair = self.data[last_idx]
            self.data[remove_idx] = last_pair
            # Update the index in the dictionary for last_pair's key.
            self.idx_map[last_pair[0]].remove(last_idx)
            self.idx_map[last_pair[0]].add(remove_idx)
        
        # Remove the last element from the list.
        self.data.pop()
        # If no more indices for key, remove key from idx_map.
        if not self.idx_map[key]:
            del self.idx_map[key]
        return True
    
    def findRandom(self) -> int:
        """
        Return a random value from the current map.
        Each pair is equally likely to be chosen,
        so the probability of a value is proportional to its frequency.
        Time: O(1).
        """
        if not self.data:
            return None
        return random.choice(self.data)[1]

# Ejemplo de uso:
rh = RandomizedHashMap()
rh.put("A", 1)
rh.put("B", 1)
rh.put("C", 2)
rh.put("A", 1)  # Duplicate key "A"
print("get('A'):", rh.get("A"))  # Ej: [1, 1]
print("findRandom():", rh.findRandom())
print("delete('B'):", rh.delete("B"))
print("get('B'):", rh.get("B"))
