class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq=[0]*100
        cnt=0
        for d0, d1 in dominoes:
            x=10*d0+d1 if d0<d1 else 10*d1+d0
            cnt+=freq[x]
            freq[x]+=1
        return cnt
        
