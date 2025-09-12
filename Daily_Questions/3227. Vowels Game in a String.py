class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(((0x208222>>(ord(c)&31))&1) for c in s)
        
