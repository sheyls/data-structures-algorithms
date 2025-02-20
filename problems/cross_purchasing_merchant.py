"""
Problem Statement:

Our company partners with many merchants, and many users make purchases at more than one merchant. We want to analyze this cross-purchasing behavior in order to recommend additional merchants to new users. You are given a list where each entry is a single user's purchase history—a list of merchants where that user has made a purchase. Your task is to analyze the dataset and determine, for every merchant that appears in at least one purchase history, which other merchant(s) most frequently appear alongside it across different users’ purchase histories.

Implement a function that takes in this list of user purchase histories and returns a mapping (dictionary) where each key is a merchant name and the corresponding value is a list of merchant names that are most frequently seen together with that key merchant. In the event of ties (i.e., multiple merchants have the same maximum frequency with the key merchant), include all of them (for example, sorted lexicographically).

Example:

Input:

python
Copy code
[
    ['Casper', 'Purple', 'Wayfair'],
    ['Purple', 'Wayfair', 'Tradesy'],
    ['Wayfair', 'Tradesy', 'Peloton']
]
Expected Output:

python
Copy code
{
    'Casper': ['Purple', 'Wayfair'],
    'Purple': ['Wayfair'],
    'Wayfair': ['Purple', 'Tradesy'],
    'Tradesy': ['Wayfair'],
    'Peloton': ['Tradesy', 'Wayfair']  # or ['Wayfair', 'Tradesy'] (order should be sorted lexicographically)
}
Notes:

A merchant should be included in the output only if it appears in at least one purchase history.
For each merchant, count the number of distinct user purchase histories in which it co-occurs with every other merchant.
If there is a tie for the highest co-occurrence with a given merchant, include all tied merchants (sorted lexicographically, if required).
Follow-Up:

How would you modify your solution if the number of users or merchants were very large?
What optimizations could be made to improve the time or space complexity of your solution?
"""

from collections import defaultdict
from typing import Dict, List


def coocurrence_purchases(names_list: List[List]) -> dict:
    coocurrences: Dict[str, Dict[str, int]] = {} # name : {"other_name": frecuency}

    for names in names_list:
        for name in names:
            if name not in coocurrences:
                coocurrences[name] = defaultdict(int)

    for names in names_list:
        unique_names = list(set(names))
        n = len(unique_names)
        for i in range(n):
            for j in range(i+1, n):
                current_name = names[i]
                next_name = names[j]

                coocurrences[current_name][next_name] += 1
                coocurrences[next_name][current_name] += 1

    cross_purchasing = {}
    for name, ocurrences in coocurrences.items():
        if ocurrences:
            max_ocurrences = max(ocurrences.values())
            cross_purchasing[name] = sorted([k for k,v in ocurrences.items() if v == max_ocurrences])
        else:
            cross_purchasing[name] = []

    return cross_purchasing

# O((LxM)^2 log(LxM)) L - outer list, M - interns list

a = [
    ['Casper', 'Purple', 'Wayfair'],
    ['Purple', 'Wayfair', 'Tradesy'],
    ['Wayfair', 'Tradesy', 'Peloton']
]

print(coocurrence_purchases(a))
