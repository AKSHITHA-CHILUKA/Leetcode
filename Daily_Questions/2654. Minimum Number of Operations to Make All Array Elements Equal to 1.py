class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n,num1,g = len(nums),0,0

        for x in nums:
            if x == 1:
                num1 += 1
            g = gcd(g, x)

        if num1 > 0:
            return n - num1
        if g > 1:
            return -1

        min_len = n
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break

        return min_len + n - 2
