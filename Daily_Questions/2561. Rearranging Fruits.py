from collections import Counter

class Solution:
    def minCost(self, basket1: list[int], basket2: list[int]) -> int:
        total_counts = Counter(basket1) + Counter(basket2)
        
        for count in total_counts.values():
            if count % 2 != 0:
                return -1
        
        fruits_to_swap = []
        count1 = Counter(basket1)
        for fruit, total_count in total_counts.items():
            target = total_count // 2
            diff = count1.get(fruit, 0) - target
            
            # if diff > 0, b1 has a surplus. if diff < 0, b2 has a surplus.
            # abs(diff) is the number of items of this fruit type in the wrong basket.
            # since each misplaced fruit corresponds to another, we add half.
            for _ in range(abs(diff)):
                fruits_to_swap.append(fruit)

        fruits_to_swap.sort()
        
        min_val = min(total_counts.keys())
        total_cost = 0
        swaps_to_make = len(fruits_to_swap) // 2
        for i in range(swaps_to_make):
            # Cost is min(direct swap cost, helper swap cost)
            total_cost += min(fruits_to_swap[i], 2 * min_val)
            
        return total_cost
