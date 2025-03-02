class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len (nums)
        numsmap = {}
        complement = 0 
        for i in range(n):
            numsmap[nums[i]] = i
        for i in range(n) : 
            complement = target - nums[i]
            if complement in numsmap and numsmap[complement]!=i:
                return [i,numsmap[complement]]
        return []
        
