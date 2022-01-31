def remove_consecutive_duplicates(s: str) -> str:
    new_word = ""
    s = s.split()
    for x in range(len(s) - 1):
        if s[x] != s[x + 1]:
            new_word += s[x] + " "
    if s[-1] != s[-2]:
        new_word += s[-1]
    return new_word


print(remove_consecutive_duplicates("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
