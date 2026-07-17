def ascii_filter(x=1, *strings, flag=True):
    results = []
    for s in strings:
        filtered = []
        for char in s:
            divisible = (ord(char) % x == 0)
            if divisible == flag:
                filtered.append(char)
        results.append(filtered)
    return tuple(results)

print(ascii_filter(2, "test", "hello", "lab002", flag=False))
