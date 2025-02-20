#House Robber: Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police (two adjacent houses cannot be robbed).

def house_robber(houses):
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]
    
    # I think this one is not necessary
    if len(houses) == 2:
        return max(houses[0], houses[1])

    rob_first = houses[0] + house_robber(houses[2:])
    skip_first = house_robber(houses[1:])
    
    max_sum = max(rob_first, skip_first)

    return max_sum

# O(2^N)

# Sol 2

def house_robber_memo(houses):
    memo = {}

    if not houses:
        return 0

    def robber(i):

        if i >= len(houses):
            return 0

        if i in memo:
            return memo[i]

        rob_first = houses[i] + robber(i + 2)
        skip_first = robber(i + 1)

        memo[i] =  max(rob_first, skip_first)

        return memo[i]

    return robber(0)

# O(N)

# Sol 3 DP
def house_robber_dp(houses):
    n = len(houses)

    if not houses:
        return 0

    dp = [0] * n

    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1], houses[i] + dp[i-2])
    
    return dp[n-1]
    
# O(N)

# Sol 4 (DP and O(1) space)

def house_robber_dp_1(houses):
    dp1 = dp2 = 0 # dp1 = dp[i-1], dp2 = dp[i-2]

    for n in houses:
        rob = max(dp1, n + dp2)
        dp1, dp2 = rob, dp1    
   
    return dp1

# O(N)

houses = [2, 7, 9, 3, 1]
print(house_robber_memo(houses)) #12
print([0] * 5)