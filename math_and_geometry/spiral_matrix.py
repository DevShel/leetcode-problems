# https://leetcode.com/problems/spiral-matrix/

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Pointers for top, right, bottom, left
        t,r,b,l = 0, len(matrix[0]) - 1, len(matrix) - 1, 0
        output = []
        curr = (0,0) # = (r,c)

        while ( l <= r and t <= b):
            # Go right
            while (curr[1] <= r):
                output.append(matrix[curr[0]][curr[1]])
                curr = (curr[0], curr[1] + 1)
            curr = (curr[0] + 1, curr[1] - 1) # Go back to rightmost boundary and go down 1

            # Go down
            while (curr[0] <= b):
                output.append(matrix[curr[0]][curr[1]])
                curr = (curr[0] + 1, curr[1])
            curr = (curr[0] - 1, curr[1] - 1) # Go back to bottom boundary and go left 1

            if (t < b):
                # Go left
                while (curr[1] >= l):
                    output.append(matrix[curr[0]][curr[1]])
                    curr = (curr[0], curr[1] - 1)
                curr = (curr[0] - 1, curr[1] + 1) # Go back to left boundary and go up 1

            if (l < r):
                # Go up
                while (curr[0] > t):
                    output.append(matrix[curr[0]][curr[1]])
                    curr = (curr[0] - 1, curr[1])
                curr = (curr[0] + 1, curr[1] + 1) # Go back to top boundary and go right 1

            t,r,b,l = t + 1, r - 1, b - 1, l + 1 # Trim off the outer layer that we just traversed
        
        return output
