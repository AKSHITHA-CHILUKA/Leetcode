class Solution(object):
    def maxCollectedFruits(self, grid):
        n = len(grid); res = 0
        for i in range(n):
            res += grid[i][i]
        for pass_ in range(2):
            if pass_ == 1:
                for i in range(n):
                    for j in range(i+1, n):
                        grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
            prev = [-1] * n; prev[n - 1] = grid[0][n - 1]
            curr = [-1] * n
            for row in range(1, n - 1):
                curr = [-1] * n
                for i in range(n):
                    if prev[i] < 0: continue
                    if i > 0: curr[i - 1] = max(curr[i - 1], prev[i] + grid[row][i - 1])
                    if i < n-1: curr[i + 1] = max(curr[i + 1], prev[i] + grid[row][i + 1])
                    curr[i] = max(curr[i], prev[i] + grid[row][i])
                prev, curr = curr, prev
            res += prev[n-1]
        return res
