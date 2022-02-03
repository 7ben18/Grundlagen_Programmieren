"""
Complete the solution so that it splits the string
into pairs of two characters. If the string contains
an odd number of characters then it should replace
the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""
test_list = ["asdfadsf", "asdfads", "s", "", "asxsd"]


def solution1(s):
    result = []
    if len(s) == "":
        return []
    elif len(s) == 1:
        return [s + "_"]
    elif len(s) % 2 == 1:
        s_new = s[0:-1]
        for i in range(0, len(s_new) - 1, 2):
            result.append(s[i] + s[i + 1])
        result.append(s[-1] + "_")
    elif len(s) % 2 == 0:
        for i in range(0, len(s) - 1, 2):
            result.append(s[i] + s[i + 1])
    return result


for x in test_list:
    print(x, solution1(x))

print()


# Codewars solution
def solution2(s):
    result = []
    if len(s) % 2:
        s += '_'
    for i in range(0, len(s), 2):
        result.append(s[i:i + 2])
    return result


# Einfach denken!
for x in test_list:
    print(x, solution2(x))

