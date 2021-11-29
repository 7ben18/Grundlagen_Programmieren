"""
Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
(At this point, the device continues from the start of the list.)
Current frequency  3, change of +1; resulting frequency  4.
Current frequency  4, change of -2; resulting frequency  2, which has already been seen.
In this example, the first frequency reached twice is 2.

What is the first frequency your device reaches twice?

-- counter start = 0
-- geht die liste zwei mal durch, die erste zahl welches 2x vorkommt ist gesucht.
-- dictionary

-- {0: 0, 1: 1, -1: 1, 2: 2, 3: 1, 4: 1}
"""

with open("testdata2018_1") as f:
    line = [int(x) for x in f.readlines()]
    #print(line)


    d = {}
    subsumme = 0
    for a in range(2):
        for i in range(len(line)):
            if subsumme in d:
                d[subsumme] += 1
            else:
                d[subsumme] = 1
            subsumme += line[i]
    #print(d)

    for key, value in d.items():
        if value == 2:
            print(key, value)
