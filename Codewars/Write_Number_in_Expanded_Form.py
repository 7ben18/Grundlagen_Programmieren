"""
You will be given a number and you will need to return it as a string in Expanded Form. For example:
expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
"""


def expanded_form(n):
    len_num = len(str(n))
    b = ""
    for index, value in enumerate(str(n)):
        if value != "0":
            b += (value + ("0" * (len_num - 1 - index)) + ",")
    return b.replace(",", " + ")[:-3]


print(expanded_form(120))

test_nums = [12, 42, 70304, 1205, 453, 23, 134, 1321, 1, 99846]
for x in test_nums:
    print(expanded_form(x))

# the struggle is real
