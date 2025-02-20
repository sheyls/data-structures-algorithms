def numTilePossibilities(tiles: str) -> int:
    dic = {}
    for t in tiles:
        if t in dic:
            dic[t] += 1 
        else: 
            dic[t] = 1
    
    def count_possibilities(dic):
        total = 0
        for t in dic:
            if dic[t] > 0:
                total += 1
                dic[t] -= 1
                total += count_possibilities(dic)
                dic[t] += 1
        return total
    
    return count_possibilities(dic)

#O(NxN!)
tiles = "AAB"
print(numTilePossibilities(tiles)) #8
tiles = "AAABBC"
print(numTilePossibilities(tiles)) #188
tiles = "V"
print(numTilePossibilities(tiles)) #1