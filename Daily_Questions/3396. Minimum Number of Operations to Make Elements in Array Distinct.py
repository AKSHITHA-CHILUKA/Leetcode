from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Initialize the number of operations counter
        operations = 0
        
        # Continue removing elements until we have distinct elements
        while len(nums) > len(set(nums)):  # Check if there are duplicates
            # Remove the first 3 elements (or fewer if there are not enough elements)
            nums = nums[3:]
            operations += 1
        
        return operations
