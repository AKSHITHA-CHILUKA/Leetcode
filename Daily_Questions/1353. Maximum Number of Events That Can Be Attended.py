def maxEvents(events):
    events.sort()
    used = [False] * 100001
    count = 0
    for s, e in events:
        for d in range(s, e + 1):
            if not used[d]:
                used[d] = True
                count += 1
                break
    return count
