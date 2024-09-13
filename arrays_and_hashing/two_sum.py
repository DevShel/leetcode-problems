from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        index = 0
        for num in nums:
            dict[num] = index
            index += 1

        index = 0
        for num in nums:
            if ((target - num) in dict and index != dict[target-num]):
                return [index, dict[target-num]]
            index += 1
