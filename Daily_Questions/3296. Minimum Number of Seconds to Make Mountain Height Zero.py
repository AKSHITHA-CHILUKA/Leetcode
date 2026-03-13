class Solution:
    def minNumberOfSeconds(self, height: int, times: list[int]) -> int:
        lo, hi = 1, 10**16

        while lo < hi:
            mid = (lo + hi) >> 1
            tot = 0
            for t in times:
                tot += int(math.sqrt(mid / t * 2 + 0.25) - 0.5)
                if tot >= height: break
            if tot >= height:
                hi = mid
            else:
                lo = mid + 1

        return lo
