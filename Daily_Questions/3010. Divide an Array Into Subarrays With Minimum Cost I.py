class Solution:
    def minimumCost(self, A: List[int]) -> int:
        a = 51
        b = 51

        for i in range(1, len(A)):
            if A[i] < a:
                b = a
                a = A[i]
            elif A[i] < b:
                b = A[i]

            if a == 1 and b == 1:
                break

        return A[0] + a + b
