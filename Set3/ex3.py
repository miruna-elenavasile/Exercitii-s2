def deep_equal(a, b):
    if type(a) != type(b):
        return False

    if isinstance(a, (int, float, str, bool)):
        return a == b

    if isinstance(a, dict):
        if len(a) != len(b):
            return False
        for key in a:
            if key not in b:
                return False
            if not deep_equal(a[key], b[key]):
                return False
        return True

    if isinstance(a, (list, tuple)):
        if len(a) != len(b):
            return False
        for x, y in zip(a, b):
            if not deep_equal(x, y):
                return False
        return True

    if isinstance(a, set):
        if len(a) != len(b):
            return False
        for x in a:
            if x not in b:
                return False
        return True

    return a == b


def compare_dicts(dict1, dict2):
    different_values = []
    only_in_first = []
    only_in_second = []

    for key in dict1:
        if key in dict2:
            if not deep_equal(dict1[key], dict2[key]):
                different_values.append(key)
        else:
            only_in_first.append(key)

    for key in dict2:
        if key not in dict1:
            only_in_second.append(key)

    return different_values, only_in_first, only_in_second
