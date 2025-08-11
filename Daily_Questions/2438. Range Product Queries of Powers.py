class Solution:
    def productQueries(self, num: int, queries: List[List[int]]) -> List[int]:
        powers = []
        while num:
            lowBit = num & -num
            powers.append(lowBit)
            num ^= lowBit

        size = len(powers)
        table = [[0] * size for _ in range(size)]
        for row, val in enumerate(powers):
            table[row][row] = val
            for col in range(row + 1, size):
                table[row][col] = (
                    table[row][col - 1] * powers[col] % (10**9 + 7)
                )

        return [table[p][q] for p, q in queries]
        
