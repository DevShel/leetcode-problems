from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        stack = []
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == "1"):
                    grid[i][j] = "2"
                    stack.append((i, j))
                    islands += 1
                    while (len(stack) > 0):
                        (r,c) = stack.pop()
                       
                        if (c > 0 and grid[r][c-1] == "1"):
                            stack.append((r, c-1))
                            grid[r][c-1] = "2"
                        if (c < len(grid[0]) - 1 and grid[r][c+1] == "1"):
                            stack.append((r, c+1))
                            grid[r][c+1] = "2"
                        if (r < len(grid) - 1 and grid[r+1][c] == "1"):
                            stack.append((r+1, c))
                            grid[r+1][c] = "2"
                        if (r > 0 and grid[r-1][c] == "1"):
                            stack.append((r - 1, c))
                            grid[r-1][c] = "2"
        return islands