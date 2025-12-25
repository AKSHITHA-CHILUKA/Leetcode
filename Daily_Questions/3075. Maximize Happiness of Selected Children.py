class Solution:
    def maximumHappinessSum(self, christmasJoy: List[int], gifts: int) -> int:
        return sum(max(0, joy - turn) for turn, joy in enumerate(sorted(christmasJoy, reverse=True)[:gifts]))
