def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def gcd_multiple(*numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = gcd(result, number)
    return result


print(gcd_multiple(12, 18, 24))
