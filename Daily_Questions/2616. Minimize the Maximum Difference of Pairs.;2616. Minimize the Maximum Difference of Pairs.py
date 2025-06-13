class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        def isValid(diff):
            cnt,i=0,1
            while i<len(nums):
                if nums[i]-nums[i-1]<=diff:
                    cnt+=1
                    i+=1
                i+=1
            return cnt>=p
            
        l,r=0,nums[-1]-nums[0]
        while l<=r:
            mid=(l+r)//2
            if isValid(mid):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
