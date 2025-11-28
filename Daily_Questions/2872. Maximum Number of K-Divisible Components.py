class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        self.ans = 0

        def dfs(node, parent):
            s = values[node]
            for nxt in adj[node]:
                if nxt != parent:
                    s += dfs(nxt, node)
            if s % k == 0:
                self.ans += 1
            return s % k

        dfs(0, -1)
        return self.ans
