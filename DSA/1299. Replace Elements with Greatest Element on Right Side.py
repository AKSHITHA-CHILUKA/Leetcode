class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        m = -1
        temp = 0
        for i in range(n-1,-1,-1):
            temp = arr[i]
            arr[i] = m 
            m = max(temp , m)
            
        return arr

        
