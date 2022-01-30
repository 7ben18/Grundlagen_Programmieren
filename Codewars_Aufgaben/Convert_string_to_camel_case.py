"""
Complete the method/function so that it converts dash/underscore
delimited words into camel casing. The first word within the output
should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""


def to_camel_case(text: str) -> str:
    text = list(text)
    for i in range(len(text)):
        if text[i] == "-" or text[i] == "_":
            text[i + 1] = text[i + 1].upper()
    word = ""
    for el in text:
        word += el
    word = word.replace("_", "").replace("-", "")

    return word


check_list = ["to_camel_case", "the-stealth-warrior", 'The-Stealth-Warrior', 'A-B-C', "A_Pippi_Was-kawaii"]
for x in check_list:
    print(to_camel_case(x))


def to_camel_case2(text):
    return text[:1] + text.title().replace("_", "").replace("-", "")[1:]


for x in check_list:
    print(to_camel_case2(x))
