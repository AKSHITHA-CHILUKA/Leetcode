class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        xMin, n=10**9, len(nums)
        maxD=-1
        for x in nums:
            if x<=xMin: xMin=x
            else: maxD=max(maxD, x-xMin)
        return maxD

        
