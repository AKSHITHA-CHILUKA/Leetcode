class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        total_length = len(s)
        z_count = s.count('z')
        
        for _ in range(t):
            total_length += z_count  
            z_count = 0
            
            
            for char in s:
                if char == 'z':
                    z_count += 1
                elif char == 'y':
                    z_count += 1  
        return total_length % MOD
