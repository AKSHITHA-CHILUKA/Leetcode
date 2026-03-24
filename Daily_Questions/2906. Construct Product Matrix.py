// This solution was implemented with assistance from ChatGPT
class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345
        n, m = len(grid), len(grid[0])
        p = [[0]*m for _ in range(n)]

        suffix = 1
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                p[i][j] = suffix
                suffix = (suffix * (grid[i][j] % MOD)) % MOD

        prefix = 1
        for i in range(n):
            for j in range(m):
                p[i][j] = (p[i][j] * prefix) % MOD
                prefix = (prefix * (grid[i][j] % MOD)) % MOD

        return p
