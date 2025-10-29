class Solution:
    def smallestNumber(self, n: int) -> int:
        i = 0
        while n & (n + 1):
            n |= 1 << i
            i += 1
        return n
