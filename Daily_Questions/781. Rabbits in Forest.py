from collections import Counter
from math import ceil

class Solution:
    def numRabbits(self, answers):
        return sum(ceil(c / (x + 1)) * (x + 1) for x, c in Counter(answers).items())
