from collections import Counter
def count_unique_duplicate(elements):
    freq = Counter(elements)

    unique = sum(1 for v in freq.values() if v == 1)
    duplicates = sum(1 for v in freq.values() if v > 1)

    return unique, duplicates
print(count_unique_duplicate([1, 2, 2, 3, 4, 4, 5]))
