def check_chain(char_len, *strings):
    for i in range(len(strings) - 1):
        current = strings[i]
        next_word = strings[i + 1]

        ending = current[-char_len:]
        beginning = next_word[:char_len]

        if ending != beginning:
            return False

    return True


print(check_chain(2, "casa", "sare", "regina"))
