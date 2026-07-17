def validate_dict(rules, dictionary):
    rules_dict = {key: (prefix, middle, suffix) for key, prefix, middle, suffix in rules}

    if set(dictionary.keys()) != set(rules_dict.keys()):
        return False

    for key, value in dictionary.items():
        prefix, middle, suffix = rules_dict[key]

        if not value.startswith(prefix):
            return False

        if not value.endswith(suffix):
            return False

        pos = value.find(middle)
        if pos == -1:
            return False

        if pos == 0 or pos + len(middle) == len(value):
            return False

    return True


# Exemplu
rules = {
    ("key1", "", "inside", ""),
    ("key2", "start", "middle", "winter")
}

d = {
    "key1": "come inside, it's too cold outside",
    "key2": "starting the engine in the middle of the winter"
}

print(validate_dict(rules, d))
