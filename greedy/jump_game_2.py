# https://leetcode.com/problems/jump-game-ii/

import sys
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        num_len = len(nums)
        if num_len == 1 or num_len == 2: return num_len - 1
        
        # Use a dp array to track our global minimum number of jumps, 
        # dp[i] is the minimum number of jumps required to reach nums[i].
        dp = [sys.maxsize] * num_len
        dp[0] = 0

        # Calculate our farthest possible jump from this index
        # We reset the farthest jump to within bounds, if it is longer than len(nums)
        farthest_jump = num_len - 1 if nums[0] >= num_len else nums[0]
        # Populate initially reachable areas
        for i in range(1, farthest_jump + 1):
            dp[i] = 1

        # Go through the entire nums array
        # Question: For each e, using our current step, 
        # would we be able to reach 'e' sooner than what 
        # is stored in our dp[] array? If so, update the dp array.
        for i in range(1, num_len):
            farthest_jump = num_len - 1 if i + nums[i] >= num_len else i + nums[i] # reset farthest jump if out of bounds 
            for j in range (i + 1, farthest_jump + 1): # For all currently reachable elements
                dp[j] = min(dp[j], dp[i] + 1) # Min the curr jump + curr distance to the curr min 

        return dp[num_len - 1]