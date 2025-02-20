def coinChange(coins, amount):
    dp = [amount+1] * (amount+1)
    dp[0] = 0

    for n in range(1,amount+1):
        for c in coins:
            if n - c >= 0:
                dp[n] = min(dp[n], dp[n-c] + 1)

    return dp[-1] if dp[-1] != amount + 1 else -1

#O(NxM)

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount)) #3