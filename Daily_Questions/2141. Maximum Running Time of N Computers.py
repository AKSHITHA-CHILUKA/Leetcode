class Solution:
    def maxRunTime(self, n: int, arr: List[int]) -> int:
        arr.sort()
        total = sum(arr)

        while arr[-1] > total // n:
            n -= 1
            total -= arr.pop()

        return total // n
