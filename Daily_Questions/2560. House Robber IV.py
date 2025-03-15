class Solution(object):
    def canRob(self, nums, mid, k):
        count = 0
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] <= mid:
                count += 1
                i += 1
            i += 1
        return count >= k

    def minCapability(self, nums, k):
        left, right = 1, max(nums)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if self.canRob(nums, mid, k):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
