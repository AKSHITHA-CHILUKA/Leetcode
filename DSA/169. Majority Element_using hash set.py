class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        res = majority = 0
        for i in nums:
            hash[i] = 1+hash.get(i,0)
            if hash[i] > majority:
                res = i
                majority = hash[i]
        return res
