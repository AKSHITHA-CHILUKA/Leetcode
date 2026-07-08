MOD, MAX = 1000000007, 100001
pow = [1] * MAX
for i in range(1, MAX):
    pow[i] = (pow[i - 1] * 10) % MOD

class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        n, res = len(s), []
        A, B, ln = [[0] * (n + 1) for _ in range(3)]

        for i in range(n):
            d = int(s[i])
            A[i + 1] = A[i] + d
            B[i + 1] = (B[i] * 10 + d) % MOD if d else B[i]
            ln[i + 1] = ln[i] + (1 if d else 0)

        res = []

        for l, r in queries:
            r += 1

            sub = (B[l] * pow[ln[r] - ln[l]]) % MOD
            x = (B[r] - sub) % MOD

            res.append((x * (A[r] - A[l])) % MOD)

        return res
