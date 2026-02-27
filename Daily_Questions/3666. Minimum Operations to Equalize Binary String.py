class Solution:
    def minOperations(self, s: str, k: int) -> int:
        zero = 0
        slen = len(s)

        for i in range(slen):
            zero += ~ord(s[i]) & 1

        if zero == 0:
            return 0

        if slen == k:
            return 1 if zero == slen else -1

        base = slen - k

        odd = max(math.ceil(zero / k), math.ceil((slen - zero) / base))

        odd += ~odd & 1

        even = max(math.ceil(zero / k), math.ceil(zero / base))

        even += even & 1

        res = float('inf')

        if (k & 1) == (zero & 1):
            res = min(res, odd)

        if (~zero & 1) == 1:
            res = min(res, even)

        return -1 if res == float('inf') else res
