class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        r, c=len(grid), len(grid[0])
        cnt, brCol=0, c
        if grid[0][0]>k:
            return 0
        cnt+=1
        for j in range(1, c):
            grid[0][j]+=grid[0][j-1]
            if grid[0][j]>k:
                brCol=j
                break
            cnt+=1
        for i in range(1, r):
            grid[i][0]+=grid[i-1][0]
            if grid[i][0]>k:
                break
            cnt+=1
            for j in range(1, brCol):
                grid[i][j]+=grid[i-1][j]+grid[i][j-1]-grid[i-1][j-1]
                if grid[i][j]>k:
                    brCol=j
                    break
                cnt+=1
        return cnt
