class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = part_sum = 0
        left = 0

        for right, num in enumerate(nums):
            part_sum += num
            while part_sum * (right - left + 1) >= k:
                part_sum -= nums[left]
                left += 1
            res += right - left + 1

        return res
