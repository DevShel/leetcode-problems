# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

import collections
from typing import List

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Maintain two deque: one that is ascending and one that is descending
        # These deque store the element values, not indices
        asc, desc = collections.deque(), collections.deque()
        max_len = 1
        left = 0

        for right, value in enumerate(nums):
            # Remove elements from the back of ascending that are larger than curr element
            while(asc and value < asc[-1]):
                asc.pop()
            asc.append(value)

            # Remove elements from the back of descending that are smaller than curr element
            while(desc and value > desc[-1]):
                desc.pop()
            desc.append(value)

            # While limit is violated, keep popping left from deque until no longer violating
            while desc[0] - asc[0] > limit:
                # Deal with the left side of the deque
                if nums[left] == desc[0]: desc.popleft()
                elif nums[left] == asc[0]: asc.popleft()
                left+=1
            max_len = max(max_len, right - left + 1)
            
        return max_len
                
            