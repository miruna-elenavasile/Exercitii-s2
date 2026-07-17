functions = {
    "print_all": lambda *a, **k: print(a, k),
    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
    "print_only_args": lambda *a, **k: print(a),
    "print_only_kwargs": lambda *a, **k: print(k)
}


def apply_function(operation, *args, **kwargs):
    if operation not in functions:
        raise ValueError("Functie inexistenta")
    return functions[operation](*args, **kwargs)


apply_function("print_all", 1, 2, 3, x=10, y=20)
apply_function("print_only_args", "Ana", "Maria")
apply_function("print_only_kwargs", nume="Ion", varsta=20)
