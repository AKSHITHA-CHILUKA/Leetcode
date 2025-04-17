class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Map to track all indices for each number
        pos = defaultdict(list)
        count = 0
        
        # Step 1: Group Genins (numbers) by village (same value)
        for i, val in enumerate(nums):
            # Step 2: Check only within the same group (same number)
            for j in pos[val]:
                if (i * j) % k == 0:
                    count += 1
            # Step 3: Add current index to the list of indices for the number
            pos[val].append(i)
        
        return count
