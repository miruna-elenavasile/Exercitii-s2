def count_occurrences(needle, haystack):
    count = 0
    start = 0

    while True:
        index = haystack.find(needle, start)
        if index == -1:
            break
        count += 1
        start = index + 1

    return count


print(count_occurrences("ab", "ababab"))
