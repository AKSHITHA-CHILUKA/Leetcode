class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        d=(0, 1, 0, -1, 0)
        r, c=len(grid), len(grid[0])
        N=r*c
        def idx(i, j):
            return i*c+j
        maxH=[-1]*N
        q=deque()
        q.append(0)
        maxH[0]=health-grid[0][0]
        while q:
            ij=q.popleft()
            curH=maxH[ij]
            if ij==N-1:
                return curH>0
            i, j=divmod(ij, c)
            for a in range(4):
                s, t=i+d[a], j+d[a+1]
                st=idx(s, t)
                if s<0 or s>=r or t<0 or t>=c:
                    continue
                H2=curH-grid[s][t]
                if H2>maxH[st]:
                    maxH[st]=H2
                    if grid[s][t]==0:
                        q.appendleft(st)
                    else:
                        q.append(st)
        return False
