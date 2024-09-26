# leetcode.com/problems/rotting-oranges

from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        overall, rotten, minutes = 0,0,0
        queue = []

        for r in range (len(grid)): 
            for c in range (len(grid[0])):
                if grid[r][c] != 0: overall += 1 # Store overall # of any-condition oranges
                if grid[r][c] == 2: 
                    rotten += 1 # Store # of rotting oranges
                    queue.append((r,c)) # Store rotting orange locations in a queue
        
        while (queue):
            new_rots = False
            for i in range (len(queue)): # Go through current wave of rots
                (r, c) = queue.pop(0) # Select an orange to work from
                # Left: rot the orange
                if (c > 0 and grid[r][c-1] == 1):
                    grid[r][c-1] = 2
                    queue.append((r, c-1))
                    rotten += 1
                    new_rots = True
                # Right: rot the orange
                if (c < len(grid[0]) - 1 and grid[r][c+1] == 1):
                    grid[r][c+1] = 2
                    queue.append((r, c+1))
                    rotten += 1
                    new_rots = True
                # Up: rot the orange
                if (r > 0 and grid[r-1][c] == 1):
                    grid[r-1][c] = 2
                    queue.append((r-1, c))
                    rotten += 1
                    new_rots = True
                # Down: rot the orange
                if (r < len(grid) - 1 and grid[r+1][c] == 1):
                    grid[r+1][c] = 2
                    queue.append((r+1, c))
                    rotten += 1
                    new_rots = True
            if (new_rots): minutes += 1 # Edge case check: we are done if there are no new rots

        # If the queue is empty, and not every orange is rotten, a fresh orange must be unreachable
        if overall != rotten: return -1  
        return minutes