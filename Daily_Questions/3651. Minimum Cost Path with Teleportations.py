class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        maxval = max(max(row) for row in grid)

        def dp_iteration(dp: list[list[int]], best_teleport: list[int]) -> list[list[int]]:
            for r in reversed(range(rows)):
                for c in reversed(range(cols)):
                    walk = math.inf if (r, c) != (rows - 1, cols - 1) else 0
                    if r + 1 < rows: walk = min(walk, dp[r + 1][c] + grid[r + 1][c])  # down
                    if c + 1 < cols: walk = min(walk, dp[r][c + 1] + grid[r][c + 1])  # right
                    dp[r][c] = min(walk, best_teleport[grid[r][c]])  # walk or teleport
            return dp

        def build_teleport(dp: list[list[int]]) -> list[int]:
            teleport = [math.inf] * (maxval + 1)

            # First build mincost for each v = value
            for r, c in product(range(rows), range(cols)):
                teleport[grid[r][c]] = min(teleport[grid[r][c]], dp[r][c])

            # Then build prefix mincost for v <= value
            for v in range(maxval + 1):
                teleport[v] = min(teleport[v], teleport[v - 1] if v > 0 else math.inf)

            return teleport

        best_teleport = [math.inf] * (maxval + 1)
        dp = [[math.inf] * cols for _ in range(rows)]
        dp[-1][-1] = 0  # zero cost to reach (m - 1, n - 1) from (m - 1, n - 1)

        for t in range(k + 1):  # t teleports allowed
            dp = dp_iteration(dp, best_teleport)
            best_teleport = build_teleport(dp)

        return dp[0][0]
