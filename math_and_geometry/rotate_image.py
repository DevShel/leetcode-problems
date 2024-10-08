# https://leetcode.com/problems/rotate-image/

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # Transpose
        # Convert rows to cols
        for r in range(len(matrix)):
            for c in range(r, len(matrix[0])):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in matrix:
            r.reverse()

        return matrix
        
        