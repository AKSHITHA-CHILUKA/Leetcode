class Solution:
    def isValid(self, word: str) -> bool:
        n=len(word)
        if n<3: return False
        vowels=1|(1<<(ord('e')-97))|(1<<(ord('o')-97))|(1<<(ord('i')-97))|(1<<(ord('u')-97))
        v=0
        for c in word:
            if  not (c.isalpha() or c.isdigit()): return False
            if c.isalpha():
                i=ord(c)-97 if ord(c)>=97 else ord(c)-65
                v|=(1<<((vowels>>i)&1))
        return v==3


        
