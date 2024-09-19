from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if (len(cost) == 2): return min(cost[0], cost[1])
        if (len(cost) == 3):
            return min(cost[0] + cost[2], cost[1])

        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        # At any point in DP, what is the cheapest up to this point
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        print(dp)
        return min(dp[-1], dp[-2])