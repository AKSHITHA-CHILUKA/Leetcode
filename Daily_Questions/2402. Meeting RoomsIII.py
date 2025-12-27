class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        free = list(range(n))
        heapq.heapify(free)
        busy = []
        cnt = [0] * n

        for s, e in meetings:
            d = e - s

            while busy and busy[0][0] <= s:
                _, r = heapq.heappop(busy)
                heapq.heappush(free, r)

            if free:
                r = heapq.heappop(free)
                heapq.heappush(busy, (e, r))
                cnt[r] += 1
            else:
                t, r = heapq.heappop(busy)
                heapq.heappush(busy, (t + d, r))
                cnt[r] += 1

        return cnt.index(max(cnt))
