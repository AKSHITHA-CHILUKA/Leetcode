class Solution(object):
    def isZeroArray(self, nums, queries):
        for l, r in queries:
            for i in range(l, r+1):
                if nums[i] > 0:
                    nums[i] -= 1
        for x in nums:
            if x != 0:
                return False
        return True
