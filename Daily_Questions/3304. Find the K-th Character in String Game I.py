class Solution:
    def kthCharacter(self, k: int) -> str:
        return chr(bin(k - 1).count("1") + 97)
        
