from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        
        dp = {}
        for coin in coins:
            dp[coin] = 1

        for i in range(amount + 1):
            for coin in coins:
                use_coin = i - coin
                if use_coin >= 0 and use_coin in dp:
                    if i in dp:
                        dp[i] = min(dp[i], 1 + dp[use_coin])
                    else:
                        dp[i] = 1 + dp[use_coin]

        return dp[amount] if (amount) in dp else -1