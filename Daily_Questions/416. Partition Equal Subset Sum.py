class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum1=sum(nums)
        if sum1&1: return False
        K=sum1//2

        @cache 
        def f(i, sum1):
            if sum1==K: return True
            if i<0 or sum1>K: return False
            return f(i-1, sum1+nums[i]) or f(i-1, sum1)
            
        return f(len(nums)-1, 0)
