"""Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd)."""


# odd = ungerade
# Die Zahl ausgeben, die ungerade mal vorkommt.


def find_it(seq: list) -> int:
    dict_zahlen = {}
    for index, value in enumerate(seq):
        value = str(value)
        if value not in dict_zahlen:
            dict_zahlen[value] = 1
        else:
            dict_zahlen[value] += 1

    for key, value in dict_zahlen.items():
        if value % 2 != 0:
            return int(key)


def find_it2(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


test_liste = [[7], [0], [1, 1, 2], [0, 1, 0, 1, 0], [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1],
              [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]]
for x in test_liste:
    print(find_it(x))
