import re
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def largest_prime_in_string(text):
    numbers = re.findall(r'\d+', text)
    largest = -1

    for num_str in numbers:
        num = int(num_str)
        if is_prime(num) and num > largest:
            largest = num

    return largest
print(largest_prime_in_string('ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'))
