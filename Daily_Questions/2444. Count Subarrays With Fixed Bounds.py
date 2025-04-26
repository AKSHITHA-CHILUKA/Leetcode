class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        pMin = pMax = bad = -1
        ans = 0
        
        for i, num in enumerate(nums):
            if num == minK:
                pMin = i
            if num == maxK:
                pMax = i
            if num < minK or num > maxK:
                bad = i
            if pMin != -1 and pMax != -1:
                ans += max(0, min(pMin, pMax) - bad)
        
        return ans
