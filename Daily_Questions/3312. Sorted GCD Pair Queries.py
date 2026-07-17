class Solution:
    def gcdValues(self, A: List[int], queries: List[int]) -> List[int]:
        mx = max(A)
        freq = [0] * (mx + 1)

        for c in A:
            freq[c] += 1

        mFreq = [0] * (mx + 1)
        pairs = [0] * (mx + 1)
        overlaps = [0] * (mx + 1)
        GCD = [0] * (mx + 1)

        for i in range(mx, 0, -1):
            sm = extra = 0
            for j in range(i, mx + 1, i):
                sm += freq[j]
                extra += GCD[j]
            
            mFreq[i] = sm
            pairs[i] = sm * (sm - 1) // 2
            overlaps[i] = extra
            GCD[i] = pairs[i] - overlaps[i]

        for i in range(1, mx + 1):
            GCD[i] += GCD[i - 1]

        return [bisect.bisect_right(GCD, c) for c in queries]
