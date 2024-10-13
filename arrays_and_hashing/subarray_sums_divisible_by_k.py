# https://leetcode.com/problems/subarray-sums-divisible-by-k/

from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0:1}
        prefix_sum = 0
        result = 0
        
        for num in nums:
            # Get the mod of our current prefix sum
            prefix_sum += num
            mod = prefix_sum % k

            # Adjust mod for negative values to always be between 0 and k-1
            mod = (mod + k) % k

            if mod in count:
                result += count[mod]
            
            # Update the count of the current modulo
            if mod in count: count[mod] = count[mod] + 1
            else: count[mod] = 1

        return result