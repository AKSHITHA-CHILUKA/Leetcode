class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k):
            for j in range(k // 2):
                grid[x + j][y + i], grid[x + k - j - 1][y + i] = grid[x + k - j - 1][y + i], grid[x + j][y + i]
        return grid

        
