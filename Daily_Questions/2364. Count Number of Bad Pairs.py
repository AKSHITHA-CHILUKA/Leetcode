class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        c=Counter(i-n for i,n in enumerate(nums))
        res=len(nums)*(len(nums)-1)
        
        for v in c.values():
            if v>1:
                res-=v*(v-1)
        return res//2
