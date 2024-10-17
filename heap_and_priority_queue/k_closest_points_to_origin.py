# https://leetcode.com/problems/k-closest-points-to-origin/

import heapq
import math
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Load up heap
        heap = []
        for (x,y) in points:
            dist = math.sqrt(math.pow(x,2) + math.pow(y,2))
            heapq.heappush(heap, (dist, x, y))

        # Pop k elements off heap
        output = []
        for i in range(k):
            (d, x, y) = heapq.heappop(heap)
            output.append([x,y])
        
        return output