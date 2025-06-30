class Solution:
    def findLHS(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return 0
        freq=Counter(nums)
        if len(freq)==1: return 0
        maxLen=0
        for x, f in freq.items():
            if x-1 in freq:
                maxLen=max(maxLen, f+freq[x-1])
        return maxLen

        
