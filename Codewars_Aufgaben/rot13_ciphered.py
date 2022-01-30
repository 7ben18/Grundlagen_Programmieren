def rot13(message):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetdict = {word: index for index, word in enumerate(alphabet, 1)}
    cipher_word = ""
    for i in message:
        if i.isalpha():
            d = i.lower()
            position = alphabetdict.get(d)
            position += 13
            new_position = position % 26

            for keys, values in alphabetdict.items():
                if new_position == values:
                    if i.isupper():
                        cipher_word += keys.upper()
                    else:
                        cipher_word += keys
        else:
            cipher_word += i
    print(cipher_word)

rot13("aAapOeai")