class Solution:
    def minMaxDifference(self, num: int) -> int:
        T=pow(10, int(log10(num)))
        seeA, seeB= False, False
        a, b, x, y=-1, -1, 0, 0
        t=T
        while t>=1:
            d, num=divmod(num, t)
            if not seeA and d!=9:
                a=d
                seeA=True
                x+=9*t
            elif seeA and d==a:
                x+=9*t
            else:
                x+=d*t
            if not seeB and d!=0:
                b=d
                seeB=True
            elif d!=b:
                y+=d*t
            t//=10
        return x-y
        
