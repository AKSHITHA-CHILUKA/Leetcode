class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        found = False
        for i in range(len(nums)+1):
            if i in nums:
                found = True
            else:
                return(i)
