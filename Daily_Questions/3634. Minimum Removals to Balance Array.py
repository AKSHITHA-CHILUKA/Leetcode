class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        if nums[0]*k>=nums[-1]: return 0
        n=len(nums)
        ans=n
        l=0
        for r, x in enumerate(nums):
            while l<r and nums[l]*k<x:
                l+=1
            ans=min(ans, n-r+l-1)
        return ans
