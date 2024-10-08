# leetcode.com/problems/top-k-frequent-elements

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for e in nums:
            if e in freq_map: freq_map[e] = freq_map[e] + 1
            else: freq_map[e] = 1
        
        unique_elements = list(freq_map.keys())
        unique_elements.sort(reverse = True, key = lambda x: freq_map[x])

        output = []
        for i in range(k):
            output.append(unique_elements[i])

        return output