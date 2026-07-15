def fibonacci(n):
    result = [0, 1]
    if n <= 0:
        return []
    if n == 1:
        return [0]

    for i in range(2, n):
        next_term = result[i - 1] + result[i - 2]
        result.append(next_term)

    return result[:n]

print(fibonacci(8))
