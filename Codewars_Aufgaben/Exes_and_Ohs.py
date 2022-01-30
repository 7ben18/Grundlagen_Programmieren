"""
Check to see if a string has the same amount of 'x's and 'o's.
The method must return a boolean and be case insensitive. The string can contain any char.
"""


def xo(s: str) -> bool:
    x_cnt = 0
    o_cnt = 0
    for i in s.lower():
        if i == "x":
            x_cnt += 1
        if i == "o":
            o_cnt += 1

    return x_cnt == o_cnt

def xo2(s: str) -> bool:
    return sum(1 for x in s.lower() if x == "x") == sum(1 for x in s.lower() if x == "o")

test_liste = ["oOxx","ooxXm","zpzpzpp","xooxx"]
for x in test_liste:
    print("function 1:", xo(x))
    print("function 2:", xo2(x))


# Codewars solution
def xo3(s):
    s = s.lower()
    return s.count('x') == s.count('o')