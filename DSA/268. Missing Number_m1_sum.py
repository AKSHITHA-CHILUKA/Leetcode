class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        Tsum = (n * (n+1)) // 2
        actual_sum = sum(nums)
        return Tsum-actual_sum
        
