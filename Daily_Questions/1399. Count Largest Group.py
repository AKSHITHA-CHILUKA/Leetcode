class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq=[0]*37
        maxF, sz=1, 1
        freq[1]=1
        for x in range(2, n+1):
            digit_sum, y=0, x
            while y>0:
                q, r=divmod(y, 10)
                digit_sum+=r
                y=q
            freq[digit_sum]+=1
            f=freq[digit_sum]
            if f==maxF: 
                sz+=1
            elif f>maxF:
                maxF=f
                sz=1
        return sz

        
