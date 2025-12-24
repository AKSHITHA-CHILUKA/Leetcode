class Solution:
    def minimumBoxes(self, apple: List[int], cap: List[int]) -> int:
        tot = sum(apple) 
        cap.sort(reverse=True)

        res = 0
        while tot > 0:
            tot -= cap[res]
            res += 1

        return res
