class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = [False] * n
        res = []
        for num in nums:
            if seen[num]:
                res.append(num)
            else:
                seen[num] = True
        return res
