class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(curr: int, n: int) -> int:
            steps = 0
            first = curr
            last = curr + 1
            
            while first <= n:
                steps += min(n + 1, last) - first
                first *= 10
                last *= 10
            
            return steps

        curr = 1
        k -= 1  # Decrement k since we start counting from 1

        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                curr += 1  # Move to the next prefix
                k -= steps  # Reduce k by the number of valid numbers skipped
            else:
                curr *= 10  # Go deeper in the current prefix
                k -= 1  # We've taken one valid number

        return curr
