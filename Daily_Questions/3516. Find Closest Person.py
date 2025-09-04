class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        return 0 if abs(x-z)==abs(y-z) else 2-(abs(x-z)<abs(y-z))
        
