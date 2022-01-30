"""
Complete the solution so that it reverses the string passed into it.
"""


def reversed_string(string: str) -> str:
    return string[::-1]


print(reversed_string("world"))


def reverse_word(string: str) -> str:
    reversed = ""
    for i in range(len(string) - 1, -1, -1):
        reversed += string[i]

    return reversed


print(reverse_word("world"))
