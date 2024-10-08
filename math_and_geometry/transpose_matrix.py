# leetcode.com/problems/transpose-matrix

from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        '''
        Considering that these matrices have the potential to be non-square,
        we must create a new matrix
        '''
        # (n x m) Matrix --> (m x n) Matrix
        r, c = len(matrix), len(matrix[0])
        # Swap the positions of r and c to create the correct size transposed matrix
        new_matrix = [[0] * r for _ in range(c)] 

        for r in range(len(matrix)): # Go over original rows
            for c in range (len(matrix[0])): # Go over original cols
                # This is not in place, so we don't have to worry about going over rows we have alr swapped
                new_matrix[c][r] = matrix[r][c] 
                

        return new_matrix
        