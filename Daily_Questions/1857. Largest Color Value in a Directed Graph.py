class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for v,u in edges: g[v].append(u)
        
        @cache
        def f(node, pending=set()):
            if node in pending: raise
            pending.add(node)
            z = Counter(colors[node])+reduce(or_,map(f,g[node]),Counter())
            pending.remove(node)
            return z

        try: return max(reduce(or_,map(f,range(len(colors)))).values())
        except: return -1
