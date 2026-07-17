operators = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b
}


def apply_operator(operator, a, b):
    if operator not in operators:
        raise ValueError("Operator invalid")
    return operators[operator](a, b)


print(apply_operator("+", 5, 3))
print(apply_operator("*", 5, 3))
print(apply_operator("/", 10, 2))
print(apply_operator("%", 10, 3))
