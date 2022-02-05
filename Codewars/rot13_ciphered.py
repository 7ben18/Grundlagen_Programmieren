"""
ROT13 is a simple letter substitution cipher that replaces a
letter with the letter 13 letters after it in the alphabet.
ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string
ciphered with Rot13. If there are numbers or special characters
included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted,
like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""
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