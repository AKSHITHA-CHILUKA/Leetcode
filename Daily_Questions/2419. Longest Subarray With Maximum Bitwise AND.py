from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """
        Finds the length of the longest subarray with the maximum possible bitwise AND.
        """
        if not nums:
            return 0
            
        # 1. Find the maximum value in the array.
        max_val = max(nums)
        
        # 2. Find the length of the longest subarray consisting only of max_val.
        max_len = 0
        current_len = 0
        
        for num in nums:
            if num == max_val:
                # If the current number is the max value, extend the current streak.
                current_len += 1
            else:
                # If the streak is broken, update the max length found so far
                # and reset the current streak length.
                max_len = max(max_len, current_len)
                current_len = 0
        
        # 3. Final check for a trailing streak.
        return max(max_len, current_len)
