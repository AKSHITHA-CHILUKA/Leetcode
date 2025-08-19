class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        return (Len:=0) or sum( Len:=Len+1 if x==0 else 0 for x in nums )
          
