from typing import List
import math

class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        # Create a dictionary to store the smallest index of each element
        element_to_index = {}
        for idx, element in enumerate(elements):
            if element not in element_to_index:
                element_to_index[element] = idx
        
        assigned = []
        for group in groups:
            min_index = float('inf')  # Track the smallest index of valid elements
            # Iterate through divisors of the group
            for divisor in range(1, int(math.sqrt(group)) + 1):
                if group % divisor == 0:
                    # Check if the divisor exists in elements
                    if divisor in element_to_index:
                        min_index = min(min_index, element_to_index[divisor])
                    # Check if the complementary divisor exists in elements
                    complementary_divisor = group // divisor
                    if complementary_divisor in element_to_index:
                        min_index = min(min_index, element_to_index[complementary_divisor])
            # If a valid element was found, assign its index; otherwise, assign -1
            if min_index != float('inf'):
                assigned.append(min_index)
            else:
                assigned.append(-1)
        return assigned©leetcode
