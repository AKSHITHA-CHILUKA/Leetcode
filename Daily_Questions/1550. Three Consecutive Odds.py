class Solution:
    def threeConsecutiveOdds(self, a: List[int]) -> bool:
        return False if len(a)<3 else any(1&a[i]&a[i+1]&a[i+2] for i in range(len(a)-2))
        
