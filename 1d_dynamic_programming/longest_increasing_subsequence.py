from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Core problem: is this a part of an increasing subsequence
        global_highest = 1
        dict = {} # <subseq length, index of curr highest num in this subsequence>
        dict[1] = 0
        for i in range(len(nums)):
            local_highest = global_highest
            while (local_highest > 0):
                if local_highest in dict and nums[dict[local_highest]] < nums[i]:
                    dict[local_highest + 1] = i
                    if (local_highest) == global_highest: global_highest += 1
                    break
                local_highest = local_highest - 1

            if (local_highest == 0):
                dict[1] = i

        return global_highest