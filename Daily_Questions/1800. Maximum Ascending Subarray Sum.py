class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum=Sum=nums[0]
        for x, y in pairwise(nums):
            Sum=y if y<=x else Sum+y
            maxSum=max(maxSum, Sum)
        return maxSum
        
