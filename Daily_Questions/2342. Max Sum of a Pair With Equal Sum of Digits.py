class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_arr = [0] * 82
        ans = -1
        for x in nums:
            digit_sum = sum(int(d) for d in str(x))
            if max_arr[digit_sum] != 0:
                ans = max(ans, x + max_arr[digit_sum])
            max_arr[digit_sum] = max(max_arr[digit_sum], x)
        return ans
