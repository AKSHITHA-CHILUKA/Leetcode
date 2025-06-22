class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        q, r =divmod(len(s), k)
        ans=[""]*(q+(r>0))
        for i in range(q):
            ans[i]=s[i*k:(i+1)*k]
        if r>0:
            ans[-1]=s[q*k:]
            ans[-1]+=fill*(k-r)
        return ans
        
