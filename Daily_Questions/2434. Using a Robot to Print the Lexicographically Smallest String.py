class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        result = []
        stack = []

        # Precompute suffix minimum characters
        min_suf = [''] * n
        min_suf[-1] = s[-1]
        for i in range(n - 2, -1, -1):
            min_suf[i] = min(s[i], min_suf[i + 1])

        for i in range(n):
            stack.append(s[i])
            # While the top of the stack is <= min character in the remaining string
            while stack and (i == n - 1 or stack[-1] <= min_suf[i + 1]):
                result.append(stack.pop())

        return ''.join(result)
