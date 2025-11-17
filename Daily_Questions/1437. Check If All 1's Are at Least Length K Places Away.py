class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n, last=len(nums), -(1<<30)
        for i, x in enumerate(nums):
            if x==1:
                if i-last-1<k: return False
                last=i
        return True
        
