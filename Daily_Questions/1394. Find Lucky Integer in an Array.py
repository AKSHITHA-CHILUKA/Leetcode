class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max((x for x, f in Counter(arr).items() if x==f), default=-1)
               
