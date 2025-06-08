class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        
        def dfs(curr):
            if curr > n:
                return
            result.append(curr)
            for i in range(10):  # Try appending 0-9
                next_num = curr * 10 + i
                if next_num > n:
                    break
                dfs(next_num)
        
        for i in range(1, 10):  # Start with 1 to 9
            if i <= n:
                dfs(i)
        
        return result
