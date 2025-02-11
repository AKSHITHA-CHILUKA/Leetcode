class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if nums[0]!=0:
            return 0
        elif nums[-1] !=n:
            return n
        for i in range(1,n):
            if nums[i]!=i:
                return i
        return 0
