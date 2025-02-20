# Given an input list of names, for each name, find the shortest substring that only appears in that name.
#
# Example:
# Input: ["cheapair", "cheapoair", "peloton", "pelican"]
# Output:
# "cheapair": "pa"  // every other 1-2 length substring overlaps with cheapoair
# "cheapoair": "po" // "oa" would also be acceptable
# "pelican": "ca"   // "li", "ic", or "an" would also be acceptable
# "peloton": "t"    // this single letter doesn't occur in any other string

from collections import defaultdict
from typing import Dict, Set


def uncommon_substring(names: list):

    str_map: Dict[str, Set[int]] = {} # for every substring the index of the word

    for index, word in enumerate(names):
        seen = set()
        for i in range(len(word)):
            for j in range(i+1, len(word)+1):
                current_substring = word[i:j]

                if current_substring not in seen:
                    seen.add(current_substring)

                    if current_substring not in str_map:
                        str_map[current_substring] = set()
                    str_map[current_substring].add(index)

    anw = {}
    for i, name in enumerate(names):
        shortest_list = ([k for k,v in str_map.items() if v == {i}])
        if shortest_list:
            shortest_list.sort(key = lambda x: len(x))
            anw[name] = shortest_list[0]
        else:
            anw[name] = ""
    
    return anw

                    
input = ["cheapair", "cheapoair", "peloton", "pelican"]
print(uncommon_substring(input))