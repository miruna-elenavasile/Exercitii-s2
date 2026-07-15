number = 2 ** 1024
number_str = str(number)
print("Ex 5:", len(number_str))

def get_max(a, b, c):
    biggest = a
    if b > biggest:
        biggest = b
    if c > biggest:
        biggest = c
    return biggest

print("Ex 6:", get_max(3, 7, 5))


def calculate(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    elif op == "/":
        return x / y

print("Ex 7:", calculate(4, 2, "+"), calculate(4, 2, "-"), calculate(4, 2, "*"), calculate(4, 2, "/"))


def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

print("Ex 8:", is_palindrome(121), is_palindrome(123))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Ex 9:", is_prime(7), is_prime(8))


def print_list(lst):
    for element in lst:
        print(element)

print("Ex 10:")
print_list([1, 2, 3, 4, 5])


def mean_and_geometric_mean(lst):
    smallest = min(lst)
    largest = max(lst)
    mean = (smallest + largest) / 2
    geometric_mean = (smallest * largest) ** 0.5
    return mean, geometric_mean

print("Ex 11:", mean_and_geometric_mean([4, 9, 2, 16, 25]))


def half_extremes(lst):
    middle = len(lst) // 2
    first_half = lst[:middle]
    second_half = lst[middle:]
    largest_in_first_half = max(first_half)
    smallest_in_second_half = min(second_half)
    return largest_in_first_half, smallest_in_second_half

print("Ex 12:", half_extremes([5, 8, 2, 9, 1, 7, 3]))

def even_digit_palindromes(lst):
    result = []
    for number in lst:
        s = str(number)
        if is_palindrome(number) and len(s) % 2 == 0:
            result.append(number)
    return result

print("Ex 13:", even_digit_palindromes([121, 1221, 1331, 12, 44, 123]))


def sublist_between_extremes(lst):
    smallest = min(lst)
    largest = max(lst)

    index_smallest = lst.index(smallest)
    index_largest = lst.index(largest)

    start = min(index_smallest, index_largest)
    end = max(index_smallest, index_largest)

    return lst[start:end + 1]

print("Ex 14:", sublist_between_extremes([5, 3, 8, 1, 9, 2]), sublist_between_extremes([5, 9, 8, 1, 3, 2]))


def diagonal_sorted_descending(matrix):
    diagonal = []
    for i in range(len(matrix)):
        diagonal.append(matrix[i][i])
    diagonal.sort(reverse=True)
    return diagonal

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Ex 15:", diagonal_sorted_descending(matrix))
