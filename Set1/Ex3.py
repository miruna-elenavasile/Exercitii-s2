def count_words(text):
    separators = " ,;?!."
    words = []
    current_word = ""

    for char in text:
        if char in separators:
            if current_word != "":
                words.append(current_word)
                current_word = ""
        else:
            current_word += char

    if current_word != "":
        words.append(current_word)

    return len(words)


print(count_words("Buna, particip la Summer Knowledge  , la AUMOVIO!"))
