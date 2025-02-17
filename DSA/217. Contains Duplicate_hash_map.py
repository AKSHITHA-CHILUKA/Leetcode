class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        num_count = {}
        for num in nums :
            if num in num_count:
                num_count[num] += 1
            else:
                num_count[num] = 1
        for num , count in num_count.items():
            if count > 1:
                return True
            elif count == 1: 
                return False
