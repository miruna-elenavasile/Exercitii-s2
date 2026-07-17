def my_zip(*lists):
    if not lists:
        return []

    max_len = max(len(lst) for lst in lists)
    result = []

    for i in range(max_len):
        current_tuple = []
        for lst in lists:
            if i < len(lst):
                current_tuple.append(lst[i])
            else:
                current_tuple.append(None)
        result.append(tuple(current_tuple))

    return result

print(my_zip([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))
