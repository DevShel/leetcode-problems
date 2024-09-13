from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1: return len(nums)
        store = set()
        for num in nums:
            store.add(num)

        global_longest = 1
        while store:
            local_longest = 1
            popped = store.pop()
            n = popped
            while n - 1 in store:
                n -= 1
                store.remove(n)
                local_longest += 1
            
            n = popped
            while n + 1 in store:
                n += 1
                store.remove(n)
                local_longest += 1

            global_longest = max(local_longest, global_longest)
            local_longest = 0

        return global_longest