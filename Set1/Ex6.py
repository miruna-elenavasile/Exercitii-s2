def camel_to_snake(text):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            if i != 0:
                result += "_"
            result += char.lower()
        else:
            result += char
    return result


print(camel_to_snake("AnaAreMere"))
