class Solution:
    def maxOperations(self, s: str) -> int:
        pref = list(accumulate(int(c) for c in s))
        return sum({pref[i] for i, c in enumerate(s) if c == '0'})

