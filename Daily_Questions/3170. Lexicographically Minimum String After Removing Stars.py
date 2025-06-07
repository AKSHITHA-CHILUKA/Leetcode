import heapq
from collections import defaultdict, deque

class Solution(object):
    def clearStars(self, s):
        n = len(s)
        pq = []  # Min-heap to store characters
        m = defaultdict(deque)  # Map character -> deque of indices
        keep = [True] * n  # Marks whether to keep character at index

        for i in range(n):
            if s[i] == '*':
                smallest = heapq.heappop(pq)  # Get smallest character
                idx = m[smallest].pop()      # Remove last occurrence index
                keep[i] = False              # Mark '*' for removal
                keep[idx] = False            # Mark smallest char for removal
            else:
                heapq.heappush(pq, s[i])
                m[s[i]].append(i)

        # Build result from characters not marked for removal
        return ''.join(s[i] for i in range(n) if keep[i])
