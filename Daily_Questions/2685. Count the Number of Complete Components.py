class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        A = defaultdict(list)
        for u, v in edges:
            A[u].append(v)
            A[v].append(u)

        vis, res = [False] * n, 0
        for i, state in enumerate(vis):
            if not state:
                E = V = 0

                def dfs(x):
                    nonlocal V, E
                    V += 1
                    E += len(A[x])
                    vis[x] = True

                    for state in A[x]:
                        if not vis[state]:
                            dfs(state)

                dfs(i)
                res += E == V * (V - 1)

        return res
