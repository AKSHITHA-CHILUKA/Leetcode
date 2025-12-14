class Solution(object):
    def numberOfWays(self, corridor):
        mod = 10**9 + 7
        s = corridor.count('S')
        if not s or s % 2:
            return 0
        ans = 1
        cnt = p = 0
        for ch in corridor:
            if ch == 'S':
                cnt += 1
                if cnt > 2 and cnt % 2:
                    ans = ans * (p + 1) % mod
                    p = 0
            elif cnt and cnt % 2 == 0:
                p += 1
        return ans
