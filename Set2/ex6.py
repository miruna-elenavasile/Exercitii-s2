def elements_in_exactly_x_lists(*lists, x):
    all_elements = []
    for lst in lists:
        for elem in lst:
            if elem not in all_elements:
                all_elements.append(elem)

    result = []
    for elem in all_elements:
        count = 0
        for lst in lists:
            if elem in lst:
                count += 1
        if count == x:
            result.append(elem)

    return result

print(elements_in_exactly_x_lists([1, 2, 3], [2, 3, 4], [4, 5, 6], [7, 1, "test"], x=2))
