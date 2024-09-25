# https://leetcode.com/problems/jump-game-ii/

import sys
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        num_len = len(nums)
        if num_len == 1 or num_len == 2: return num_len - 1
        
        dp = [sys.maxsize] * num_len
        dp[0] = 0

        farthest_jump = num_len - 1 if nums[0] >= num_len else nums[0]
        # Populate initially reachable areas
        for i in range(1, farthest_jump + 1):
            dp[i] = 1

        # Core recursive step: what is the minimum number of jumps needed to get to the current element
        for i in range(1, num_len):
            if (dp[i] != sys.maxsize): # If we are able to reach this element through our jumps
                farthest_jump = num_len - 1 if i + nums[i] >= num_len else i + nums[i] # reset farthest jump if out of bounds 
                for j in range (i + 1, farthest_jump + 1): # For all currently reachable elements
                    dp[j] = min(dp[j], dp[i] + 1) # Min the curr jump + curr distance to the curr min 

        return dp[num_len - 1]