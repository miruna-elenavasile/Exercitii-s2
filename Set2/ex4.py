def compare_lists(a, b):
    intersection = []
    for element in a:
        if element in b and element not in intersection:
            intersection.append(element)

    union = []
    for element in a + b:
        if element not in union:
            union.append(element)

    a_minus_b = []
    for element in a:
        if element not in b and element not in a_minus_b:
            a_minus_b.append(element)

    b_minus_a = []
    for element in b:
        if element not in a and element not in b_minus_a:
            b_minus_a.append(element)

    return intersection, union, a_minus_b, b_minus_a

print(compare_lists([1, 2, 3, 4], [3, 4, 5, 6]))
