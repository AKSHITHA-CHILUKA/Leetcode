def maxFreeTime(eventTime, startTime, endTime):
    n = len(startTime)
    if n == 0:
        return eventTime

    gaps = [0] * (n + 1)
    gaps[0] = startTime[0]

    for i in range(1, n):
        gaps[i] = startTime[i] - endTime[i - 1]
    gaps[n] = eventTime - endTime[n - 1]

    largestRight = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        largestRight[i] = max(largestRight[i + 1], gaps[i + 1])

    maxFree = 0
    largestLeft = 0

    for i in range(1, n + 1):
        duration = endTime[i - 1] - startTime[i - 1]
        canFitLeft = largestLeft >= duration
        canFitRight = largestRight[i] >= duration

        if canFitLeft or canFitRight:
            merged = gaps[i - 1] + gaps[i] + duration
            maxFree = max(maxFree, merged)

        maxFree = max(maxFree, gaps[i - 1] + gaps[i])
        largestLeft = max(largestLeft, gaps[i - 1])

    return maxFree
