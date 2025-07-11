def mostBooked(n, meetings):
    busy = [0] * n  # End time of each room
    count = [0] * n  # Number of times each room is booked

    meetings.sort()

    for start, end in meetings:
        earliest = float('inf')
        roomIndex = -1
        assigned = False

        for i in range(n):
            if busy[i] < earliest:
                earliest = busy[i]
                roomIndex = i
            if busy[i] <= start:
                busy[i] = end
                count[i] += 1
                assigned = True
                break

        if not assigned:
            busy[roomIndex] += end - start
            count[roomIndex] += 1

    maxCount = max(count)
    return count.index(maxCount)
