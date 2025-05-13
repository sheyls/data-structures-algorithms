from collections import defaultdict

memo = defaultdict(int)

memo[1] = 1
memo[2] = 2

#top-down
def extraLongFactorials(n):
    if memo[n]:
        return memo[n]
    
    memo[n]  = n * extraLongFactorials(n-1)
    
    return memo[n]
    

#bottom-up
def extraLongFactorials2(n):
    for i in range(3,n+1):
        if not memo[n]:
            memo[i] = i * memo[i-1]
    
    return memo[n]

# Test cases
print(extraLongFactorials(25)) #15511210043330985984000000
print(extraLongFactorials2(25)) #15511210043330985984000000
