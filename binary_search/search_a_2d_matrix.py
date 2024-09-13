from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, (len(matrix)*len(matrix[0]) - 1)
        while (l <= r):
            mid = (r+l)//2
            mid_row = mid // len(matrix[0])
            mid_col = mid - (mid_row)*len(matrix[0])
            mid_val = matrix[mid_row][mid_col]

            if ( mid_val == target):
                return True
            elif (mid_val < target):
                l = mid + 1    
            else:
                r = mid - 1
        return False