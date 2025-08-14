class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count=0
        prev='X'
        maxd=' '
        for c in num:
            if c==prev: count+=1
            else: count=1
            if count==3: maxd=max(c, maxd)
            prev=c
        if maxd==' ': return ""
        return maxd*3
