MOD = 1_000_000_007
MAXN = 1000
fact = [0] * (MAXN + 1)
invfact = [0] * (MAXN + 1)

def init():
    fact[0] = 1
    for i in range(1, MAXN + 1):
        fact[i] = (fact[i - 1] * i) % MOD
    invfact[MAXN] = pow(fact[MAXN], MOD - 2, MOD)
    for i in range(MAXN, 0, -1):
        invfact[i - 1] = (invfact[i] * i) % MOD

init()

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        zero, one = min(zero, one), max(zero, one)

        if limit == 1:
            if zero == one: return 2
            if zero + 1 == one: return 1
            return 0

        def ncr(n: int, r: int) -> int:
            return fact[n] * invfact[r] * invfact[n - r]

        @cache
        def ways(n: int, k: int) -> int:
            if n == k: return 1
            j, total, flag = 0, 0, True
            while j <= k <= n:
                term = ncr(k, j) * ncr(n - 1, k - 1)
                total = total + term if flag else total - term
                n -= limit
                j += 1
                flag = not flag
            return total

        result = 0
        start = (zero + limit - 1) // limit
        prv, cur, nxt = 0, ways(one, start), ways(one, start + 1)

        for k in range(start, zero + 1):
            result += (prv + 2 * cur + nxt) * ways(zero, k)
            prv, cur, nxt = cur, nxt, ways(one, k + 2)

        ways.cache_clear()
        return result % MOD
