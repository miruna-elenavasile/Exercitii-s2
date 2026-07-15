import re
def evaluate_polynomial(poly, x):
    poly = poly.replace(" ", "")
    if poly[0] not in "+-":
        poly = "+" + poly

    pattern = r'([+-])(\d*)(x)?(\^(\d+))?'
    total = 0

    for match in re.finditer(pattern, poly):
        sign, coef, has_x, _, power = match.groups()

        coef = int(coef) if coef != "" else 1
        if sign == "-":
            coef = -coef

        if has_x:
            power = int(power) if power else 1
        else:
            power = 0

        total += coef * (x ** power)
    return total

print(evaluate_polynomial("3x ^ 3 + 5x ^ 2 - 2x - 5", 2))  # 35
