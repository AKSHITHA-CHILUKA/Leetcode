class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n=len(points)
        maxA=0
        for i in range(n-2):
            a0, a1=points[i]
            for j in range(i+1, n-1):
                b0, b1=points[j]
                for k in range(j+1, n):
                    c0, c1=points[k]
                    area=(b0-a0)*(c1-a1)-(b1-a1)*(c0-a0)
                    maxA=max(maxA, abs(area))
        return 0.5*maxA
        
