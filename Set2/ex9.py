def sort_by_third_char(lst):
    return sorted(lst, key=lambda t: t[1][2])

print(sort_by_third_char([('abc', 'bcd'), ('abc', 'zza')]))
