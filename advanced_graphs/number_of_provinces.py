# https://leetcode.com/problems/number-of-provinces

# Very simple union find without path compression or weighting
from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    # Go recursively up tree to find the parent/representative of the cluster
    def find(self, x): 
        if self.parent[x] != x: return self.find(self.parent[x])
        else: return x
    
    # Find parents of each cluster. If not equal, set one to be the other
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if (root_x != root_y): self.parent[root_x] = root_y

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num_provinces = 0
        uf = UnionFind(len(isConnected))

        for r in range(len(isConnected)):
            for c in range(len(isConnected[0])):
                if isConnected[r][c] == 1:
                    uf.union(r,c)
        
        # Get number of unique roots
        unique_roots = set()
        for i in range(len(isConnected)):
            unique_roots.add(uf.find(i))
        
        return len(unique_roots)