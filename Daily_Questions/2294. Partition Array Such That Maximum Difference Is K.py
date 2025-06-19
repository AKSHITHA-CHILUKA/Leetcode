class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        min_val = nums[0]
        for num in nums[1:]:
            if num - min_val > k:
                ans += 1
                min_val = num
        return ans
