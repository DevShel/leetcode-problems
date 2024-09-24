from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # We must partition the elements in a way that they are equal to half of the total sum
        # Furthermore, this total sum must not be odd

        if len(nums) == 1: return False
        total = 0
        for n in nums:
            total += n
        if (total % 2 != 0): return False


        all_sums = set()
        all_sums.add(nums[0])

        '''
        At each index in our array, add the current element to all previous possible sums
        then check if half of the total sum is in the output set
        '''
        for i in range(1, len(nums)):
            curr_sums = set()
            for sum in all_sums:
                curr_sums.add(sum + nums[i])
            all_sums.update(curr_sums)

        return (total/2 in all_sums)