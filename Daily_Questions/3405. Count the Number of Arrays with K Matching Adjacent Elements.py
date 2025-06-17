class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # Solution 2: Slightly More Efficient
        mod, d = 10**9 + 7, n - 1
        if k > d:       return 0
        r, C = k, 1
        if r > d - r:   r = d - r
        if r:
            inv = [0] * (r + 1)
            inv[1] = 1
            for i in range(2, r + 1):
                inv[i] = mod - (mod // i) * inv[mod % i] % mod
            for i in range(1, r + 1):
                C = C * (d - r + i) % mod * inv[i] % mod
        return m * C % mod * pow(m - 1, d - k, mod) % mod




        # Solution 1: First Solution
        def comb(a, b):
            return fac[a] * inv[b] % mod * inv[a - b] % mod if 0 <= b <= a else 0

        mod = 10**9 + 7
        if k > n - 1:
            return 0

        fac = [1] * n
        for i in range(1, n):
            fac[i] = fac[i - 1] * i % mod

        inv = [1] * n
        inv[n - 1] = pow(fac[n - 1], mod - 2, mod)
        for i in range(n - 1, 0, -1):
            inv[i - 1] = inv[i] * i % mod

        return m * comb(n - 1, k) % mod * pow(m - 1, n - 1 - k, mod) % mod
