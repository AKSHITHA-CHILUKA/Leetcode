class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s=0
        for i in set(nums) :
            if i >0:
                s+=i
        if s==0:
            return max(nums)
        return s
