class Solution:
    DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    def lenOfVDiagonal(self, grid):
        m, n = len(grid), len(grid[0])
        memo = [[[0] * (1 << 3) for _ in range(n)] for _ in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                maxs = [m - i, j + 1, i + 1, n - j]
                for k in range(4):
                    if maxs[k] > ans:
                        ans = max(ans, self.dfs(i, j, k, 1, 2, grid, memo) + 1)
        return ans

    def dfs(self, i, j, k, canTurn, target, grid, memo):
        m, n = len(grid), len(grid[0])
        i += self.DIRS[k][0]
        j += self.DIRS[k][1]
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != target:
            return 0

        mask = (k << 1) | canTurn
        if memo[i][j][mask] > 0:
            return memo[i][j][mask]

        res = self.dfs(i, j, k, canTurn, 2 - target, grid, memo)
        if canTurn == 1:
            maxs = [m - i - 1, j, i, n - j - 1]
            nk = (k + 1) % 4
            if maxs[nk] > res:
                res = max(res, self.dfs(i, j, nk, 0, 2 - target, grid, memo))
        memo[i][j][mask] = res + 1
        return memo[i][j][mask]
