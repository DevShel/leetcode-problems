from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)
        return self.rob_helper(nums, 0, dp)

    def rob_helper(self, nums, i, dp):
        if (dp[i] != -1): return dp[i]
        if i == len(nums) - 1: return nums[i]
        if i == len(nums) - 2: return max(nums[i], nums[i+1])
        dp[i] = max(nums[i] + self.rob_helper(nums, i + 2, dp), self.rob_helper(nums, i + 1, dp))
        return dp[i]
    