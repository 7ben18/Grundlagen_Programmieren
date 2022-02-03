"""
Write a function that will return the count of distinct
case-insensitive alphabetic characters and numeric digits
that occur more than once in the input string. The input
string can be assumed to contain only alphabets
(both uppercase and lowercase) and numeric digits.
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""


def duplicate_count(text):
    diction = {}
    for index, value in enumerate(text.lower()):
        if value not in diction:
            diction[value] = 1
        else:
            diction[value] += 1
    cnt = 0
    for key, value in diction.items():
        if value > 1:
            cnt += 1
    return cnt

test_words = ["asgbASgaew","abcde","abcdeaa","abcdeaB","Indivisibilities","indivisibility"]
for x in test_words:
    print(x, "->", duplicate_count(x))