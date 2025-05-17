class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        i = 0
        j = 0
        h = n-1
        temp = 0
        while(i <= h):
            if nums[i] == 0 :
                temp = nums[i]
                nums[i] =nums[j]
                nums[j] = temp 
                i += 1
                j += 1
            elif nums[i] == 2:
                temp =  nums[i]
                nums[i] = nums[h]
                nums[h] = temp
                h -=1
            else:
                i += 1

        
