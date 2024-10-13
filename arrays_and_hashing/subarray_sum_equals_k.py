# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # <prefix sum value, frequency>
        prefix_map = {0:1}
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num

            # We must find if there are any previous prefix sums that we 
            # can subtract from our current sum, in order to get k
            value_to_remove_from_curr_sum = prefix_sum - k

            # Add to our result, the number of times we have encountered the sum we are looking to remove from our current sum
            if value_to_remove_from_curr_sum in prefix_map:
                result += prefix_map[value_to_remove_from_curr_sum]
            
            # Update our prefix sum map
            if prefix_sum in prefix_map:
                prefix_map[prefix_sum] = prefix_map[prefix_sum] + 1
            else:
                prefix_map[prefix_sum] = 1
            
        return result 
