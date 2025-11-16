class Solution:
    def numSub(self, s: str) -> int:
        mod = int(10 ** 9 + 7)
        ans = 0

        count = 0
        for i in range(len(s)):
            if(s[i] == "1"):
                count += 1
            else:
                ans += ((count * (count + 1)) // 2) % mod
                count = 0
        
        ans += ((count * (count + 1)) // 2) % mod
        
        return ans
