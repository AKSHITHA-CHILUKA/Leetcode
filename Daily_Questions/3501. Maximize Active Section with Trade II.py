class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        ones = s.count('1')

        # maximal zero-blocks (inclusive ends), unzipped into starts / ends
        zs, ze = zip(*((mo.start(), mo.end() - 1) for mo in re.finditer('0+', s))) if '0' in s else ((), ())
        nblocks = len(zs)

        # valley j: full value = sum of the two adjacent run lengths
        V = list(map(sum, pairwise(b - a + 1 for a, b in zip(zs, ze))))

        # sparse table for range-max over V
        nv = len(V)
        sparse = [V]
        half = 1
        while half * 2 <= nv:
            prev = sparse[-1]
            sparse.append(list(map(max, prev, prev[half:])))
            half *= 2

        def rmq(lo, hi):                              # inclusive max over V[lo..hi]
            t = (hi - lo + 1).bit_length() - 1
            return max(sparse[t][lo], sparse[t][hi - (1 << t) + 1])

        def clip(j, l, r):                            # valley j's gain, clipped to [l, r]
            return V[j] - max(0, l - zs[j]) - max(0, ze[j + 1] - r)

        def gain(l, r):
            if nblocks < 2:
                return 0
            ja = bisect_left(ze, l)                   # first usable valley: left run ends >= l
            jb = bisect_right(zs, r) - 2              # last  usable valley: right run starts <= r
            if ja > jb:
                return 0
            return max(clip(ja, l, r), clip(jb, l, r), rmq(ja + 1, jb - 1) if jb - ja >= 2 else 0)

        return [ones + gain(l, r) for l, r in queries]
