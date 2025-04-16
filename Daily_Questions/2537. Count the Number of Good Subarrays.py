class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        freq = defaultdict(int)  # Kakashi’s logbook
        left = 0
        pairs = 0
        ans = 0

        # Naruto dashes through nums
        for right in range(len(nums)):
            val = nums[right]
            pairs += freq[val]  # More clones = more support pairs
            freq[val] += 1

            # While support ≥ k, Sasuke trims front
            while pairs >= k:
                ans += len(nums) - right
                out = nums[left]
                freq[out] -= 1
                pairs -= freq[out]
                left += 1
        return ans
