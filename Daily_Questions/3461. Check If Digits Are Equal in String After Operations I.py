class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(digit) for digit in s]  # converting to int array for easy manipulation
        while len(digits) > 2:
            newS = []  # this variable will hold the resulting array after this step
            for pos in range(0,len(digits)-1):
                # iterating through the current digits for pairwise sum
                pairSum = digits[pos] + (digits[pos+1] if pos+1 < len(s) else 0)
                newS.append(pairSum % 10)  # adding digit to result
            digits = newS


        return digits[0] == digits[1]
