class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        if r < 3 or c < 3:
            return 0

        ans = 0
        for i in range(r - 2):
            for j in range(c - 2):
                used = [False] * 10
                ok = True

                for x in range(3):
                    for y in range(3):
                        v = grid[i + x][j + y]
                        if v < 1 or v > 9 or used[v]:
                            ok = False
                            break
                        used[v] = True
                    if not ok:
                        break
                if not ok:
                    continue

                s = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                for x in range(3):
                    if grid[i+x][j] + grid[i+x][j+1] + grid[i+x][j+2] != s:
                        ok = False
                for y in range(3):
                    if grid[i][j+y] + grid[i+1][j+y] + grid[i+2][j+y] != s:
                        ok = False
                if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != s:
                    ok = False
                if grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != s:
                    ok = False

                if ok:
                    ans += 1

        return ans
