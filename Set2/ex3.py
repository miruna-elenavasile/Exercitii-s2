from math import gcd
from itertools import combinations

def unique_lines(points):
    lines = set()

    for (x1, y1), (x2, y2) in combinations(points, 2):
        a = y2 - y1
        b = x1 - x2
        c = -(a * x1 + b * y1)

        divisor = gcd(gcd(abs(a), abs(b)), abs(c))
        if divisor == 0:
            divisor = 1

        a //= divisor
        b //= divisor
        c //= divisor

        if a < 0 or (a == 0 and b < 0):
            a, b, c = -a, -b, -c

        lines.add((a, b, c))

    return list(lines)

print(unique_lines([(0, 0), (1, 1), (2, 2), (0, 1)]))
