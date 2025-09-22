class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
         return reduce(mul, max(Counter(Counter(nums).values()).items()))
