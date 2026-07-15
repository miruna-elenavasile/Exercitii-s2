def has_special_characters(text):
    special_chars = "\r\t\n\a\b\f\v"
    for char in text:
        if char in special_chars:
            return True
    return False


print(has_special_characters("ana\t are \a mere"))
