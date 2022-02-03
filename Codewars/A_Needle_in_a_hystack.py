"""
Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:
"""


def find_needle(L: list) -> str:
    for index, value in enumerate(L):
        if value == "needle":
            return "found the needle at position " + str(index)


print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))

l = ['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']
for index, value in enumerate(l):
    print(index, value)
