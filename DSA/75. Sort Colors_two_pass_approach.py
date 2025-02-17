class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        start = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i] , nums[start] = nums[start] ,nums[i]
                start +=1
        for i in range(start, n):
            if nums[i] == 1:
                nums[i] , nums[start] = nums[start] ,nums[i]
                start +=1
