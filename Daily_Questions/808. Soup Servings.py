class Solution:
    def soupServings(self, n: int) -> float:
        if n>50000: return 1.0
        @cache
        def dfs(A, B):
            if A<=0 and B>0: return 1
            if A<=0 and B<=0: return 0.5
            if A>0 and B<=0: return 0
            return 0.25*(dfs(A-4, B)+dfs(A-3, B-1)+dfs(A-2, B-2)+dfs(A-1, B-3))
        N=(n+24)//25
        return dfs(N, N)
        
