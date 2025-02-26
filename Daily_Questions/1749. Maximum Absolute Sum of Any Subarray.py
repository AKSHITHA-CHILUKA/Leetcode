class Solution:
    def maxAbsoluteSum(self, nums):
        sum, minSum, maxSum = 0, 0, 0
        for num in nums:
            sum += num
            maxSum = max(maxSum, sum)
            minSum = min(minSum, sum)
        return abs(maxSum - minSum)
