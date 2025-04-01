from typing import List

class Solution:
    def rec(self, i: int, questions: List[List[int]], dp: List[int], n: int) -> int:
        if i >= n:
            return 0
        if dp[i] != -1:
            return dp[i]

        take = questions[i][0] + self.rec(i + questions[i][1] + 1, questions, dp, n)
        dont = self.rec(i + 1, questions, dp, n)

        dp[i] = max(take, dont)
        return dp[i]

    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [-1] * n
        return self.rec(0, questions, dp, n)
