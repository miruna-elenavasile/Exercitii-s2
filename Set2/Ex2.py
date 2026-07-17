def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(numbers):
    result = []
    for number in numbers:
        if is_prime(number):
            result.append(number)
    return result

print(get_primes([4, 7, 10, 13, 15, 17, 20]))
