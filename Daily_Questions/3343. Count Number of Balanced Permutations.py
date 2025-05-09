MOD = 10**9 + 7

class Solution:
    def __init__(self):
        self.fact = []
        self.inv = []
        self.invFact = []

    def precompute(self, n):
        self.fact = [1] * (n + 1)
        self.inv = [1] * (n + 1)
        self.invFact = [1] * (n + 1)

        for i in range(1, n + 1):
            self.fact[i] = self.fact[i - 1] * i % MOD

        for i in range(2, n + 1):
            self.inv[i] = MOD - MOD // i * self.inv[MOD % i] % MOD

        for i in range(1, n + 1):
            self.invFact[i] = self.invFact[i - 1] * self.inv[i] % MOD

    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        digit_values = [int(c) for c in num]
        total_sum = sum(digit_values)

        if total_sum % 2 == 1:
            return 0

        self.precompute(n)

        half_sum = total_sum // 2
        half_len = n // 2

        dp = [[0] * (half_len + 1) for _ in range(half_sum + 1)]
        dp[0][0] = 1

        digit_count = [0] * 10
        for d in digit_values:
            digit_count[d] += 1
            for s in range(half_sum, d - 1, -1):
                for l in range(half_len, 0, -1):
                    dp[s][l] = (dp[s][l] + dp[s - d][l - 1]) % MOD

        res = dp[half_sum][half_len]
        res = res * self.fact[half_len] % MOD
        res = res * self.fact[n - half_len] % MOD

        for cnt in digit_count:
            res = res * self.invFact[cnt] % MOD

        return res
