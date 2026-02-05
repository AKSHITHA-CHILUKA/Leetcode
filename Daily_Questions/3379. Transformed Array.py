class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        return [nums[(i+nums[i])%len(nums)] for i  in range(len(nums))]
        
