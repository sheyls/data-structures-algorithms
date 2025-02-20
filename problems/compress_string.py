# Implement compress() and decompress() functions for a basic string compression scheme. In particular, we would like to compress strings with long runs of the same character, for example "aaaaaabbbbbbccdddd".

def compress(word: str) -> str:

    if not word:
        return ""

    n = len(word)
    i = 0
    result = []

    while i < n:
        count = 1
        current_char = word[i]
        while i + 1 < n and current_char == word[i+1]:        
            count += 1
            i += 1
                
        if count == 1:
            result.append(word[i])
        else:
            result.append(f"{word[i]}{count}")

        i += 1
    
    return "".join(result)

def decompress(word: str) -> str:

    result = ""
    n = len(word)
    i = 0

    while i < n:
        char = word[i]
        i += 1

        num = ""
        while i < n and word[i].isnumeric():
            num += word[i]
            i += 1
        
        count = int(num) if num else 1

        result += char * count
    
    return result
    
s = "aaaaaabbbbbbccdddd"
print(s)
c = compress(s)
print(c)
print(decompress(c))