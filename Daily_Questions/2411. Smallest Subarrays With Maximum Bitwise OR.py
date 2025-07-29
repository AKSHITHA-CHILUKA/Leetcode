class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        # Step 2: Initialize latest array to track last seen position of each bit
        latest = [-1] * 32

        # Step 3: Traverse the array from right to left
        for i in range(n - 1, -1, -1):
            farthest = i  # Default: subarray ends at i

            # Step 4: Update latest seen positions for bits set in nums[i]
            for b in range(32):
                if (nums[i] >> b) & 1:
                    latest[b] = i

                # Step 5: For each bit, if seen, update farthest position needed
                if latest[b] != -1:
                    farthest = max(farthest, latest[b])

            # Step 6: Store the length of smallest subarray starting at i
            result[i] = farthest - i + 1

        # Step 7: Return the result array
        return result 
