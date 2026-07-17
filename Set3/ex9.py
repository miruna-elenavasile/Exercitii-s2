from itertools import combinations
def set_operations(*sets):
    result = {}

    for a, b in combinations(sets, 2):
        result[f"{a} | {b}"] = len(a | b)
        result[f"{a} & {b}"] = len(a & b)
        result[f"{a} - {b}"] = len(a - b)
        result[f"{b} - {a}"] = len(b - a)

    return result

print(set_operations({1, 2}, {2, 3}, {1, 3, 4}))
