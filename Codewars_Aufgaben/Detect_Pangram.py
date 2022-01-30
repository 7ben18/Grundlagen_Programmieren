"""
A pangram is a sentence that contains every single letter
of the alphabet at least once. For example, the sentence
"The quick brown fox jumps over the lazy dog"
is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram.
Return True if it is, False if not. Ignore numbers and punctuation.
"""
def is_pangram(s):
    abc_ = "abcdefghijklmnopqrstuvwxyz"

    # creating a dictionary of letters as key and their value as zero
    dict_abc = {key: 0 for value, key in enumerate(abc_)}

    # iterating through the parameter to get every letter from the word
    for i in s.lower():
        # checking if its a number or punctuation
        if i.isalpha():
            # add +1 for the letter
            dict_abc[i] += 1

    # get every value from the dictionary and pack it in a list
    values = list(dict_abc.values())
    if 0 in values:
        return False
    else:
        return True


check_sentence = ["How quickly daft jumping zebras vex. is a pangram", "ais1234rdfg",
                  "Aacdefghijklmnopqrstuvwxyz", "This isn't a pangram!",
                  "The quick brown fox jumps over the lazy dog"]

for i in check_sentence:
    print("Function 1:", is_pangram(i))

# Codewars solution
import string

def is_pangram2(s):
    return set(string.lowercase) <= set(s.lower())

for i in check_sentence:
    print("Function 2:", is_pangram2(i))


