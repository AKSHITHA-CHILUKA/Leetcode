class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n=len(dominoes)
        L=[0]*n
        F=0
        for i in range(n-1, -1, -1):
            c=dominoes[i]
            if c=='L': F=n
            elif c=='R': F=0
            else: F-=(F>0)
            L[i]=F
        F=0
        D=list(dominoes)
        for i, c in enumerate(D):
            if c=='L': F=0
            elif c=='R': F=n
            else:
                F-=(F>0)
                if F>L[i]: D[i]='R'
                elif F<L[i]: D[i]='L'
                else: D[i]='.'
        return "".join(D)
        
