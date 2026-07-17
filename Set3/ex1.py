def compare_as_sets(a, b):
    set_a = set(a)
    set_b = set(b)

    intersection = set_a & set_b
    union = set_a | set_b
    a_minus_b = set_a - set_b
    b_minus_a = set_b - set_a

    return intersection, union, a_minus_b, b_minus_a

print(compare_as_sets([1, 2, 3, 4], [3, 4, 5, 6]))
