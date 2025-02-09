from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        # Sort the bottom-left triangle (including the middle diagonal)
        for d in range(n):
            diagonal = []
            i = d
            j = 0
            while i < n and j < n:
                diagonal.append(grid[i][j])
                i += 1
                j += 1
            diagonal.sort(reverse=True)
            i = d
            j = 0
            idx = 0
            while i < n and j < n:
                grid[i][j] = diagonal[idx]
                i += 1
                j += 1
                idx += 1
        
        # Sort the top-right triangle
        for d in range(1, n):
            diagonal = []
            i = 0
            j = d
            while i < n and j < n:
                diagonal.append(grid[i][j])
                i += 1
                j += 1
            diagonal.sort()
            i = 0
            j = d
            idx = 0
            while i < n and j < n:
                grid[i][j] = diagonal[idx]
                i += 1
                j += 1
                idx += 1
        
        return grid©leetcode
