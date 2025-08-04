def totalFruit(fruits):
    last = second_last = -1
    last_count = curr = res = 0

    for f in fruits:
        if f == last or f == second_last:
            curr += 1
        else:
            curr = last_count + 1

        if f == last:
            last_count += 1
        else:
            last_count = 1
            second_last, last = last, f

        res = max(res, curr)

    return res
