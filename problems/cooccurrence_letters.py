# Given an input list of strings, for each letter appearing anywhere 
# in the list, find the other letter(s) that appear in the most 
# number of words with that letter.

from typing import Dict, List

# First idea (Wrong)
def cooccurrence_letters(words: List[str]):
    sol = {} # 'a':{l: 2}

    for w in words:
        wo = w
        for idl in range(len(wo)):
            current_letter = w[idl]

            if current_letter not in sol:
                sol[current_letter] = {}
            
            for idp in range(0, idl):
                prev_letter = wo[idp]
                if current_letter in sol[prev_letter]:
                    sol[prev_letter][current_letter] += 1
                else:
                    sol[prev_letter][current_letter] = 1

                if prev_letter in sol[current_letter]:
                    sol[current_letter][prev_letter] += 1
                else:
                    sol[current_letter][prev_letter] = 1
            
    answer = {}
    for letter, counts in sol.items():
        if counts: 
            max_count = max(counts.values())
            answer[letter] = sorted([other for other, cnt in counts.items() if cnt == max_count])
        else:
            answer[letter] = []
    print(sol)

    return answer
            

# Sol

def letter_cooccurrence(words: List[str]) -> Dict[str, List[str]]:
    coocurrence = {} # 'a' : {'b': 1}
    
    for word in words:
        unique_letters = list(set(word))

        n = len(unique_letters)

        for letter in unique_letters:
            if letter not in coocurrence:
                coocurrence[letter] = {}

        for i in range(n):
            for j in range(i+1, n):
                a = unique_letters[i]
                b = unique_letters[j]
                coocurrence[a][b] = coocurrence[a].get(b,0) + 1
                coocurrence[b][a] = coocurrence[b].get(a,0) + 1

    ans = {}
    for letter, count in coocurrence.items():
        if count:
            max_count = max(count.values())
            final_letters = sorted([k for k,v in count.items() if v == max_count])
            ans[letter] = final_letters
        else:
            ans[letter] = []

    return ans

words = ['abc', 'bcd', 'cde']
print(letter_cooccurrence(words))