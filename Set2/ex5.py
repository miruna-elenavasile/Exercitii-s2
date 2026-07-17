def combinations(x, k):
    if k == 0:
        return [()]
    if k > len(x):
        return []

    result = []
    for i in range(len(x)):
        first = x[i]
        rest = x[i + 1:]

        for smaller_combination in combinations(rest, k - 1):
            result.append((first,) + smaller_combination)

    return result

print(combinations([1, 2, 3, 4], 3))
