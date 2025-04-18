class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n - 1):
            temp, i = "", 0
            while i < len(res):
                count = 1
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    i += 1
                    count += 1
                temp += str(count) + res[i]
                i += 1
            res = temp
        return res
