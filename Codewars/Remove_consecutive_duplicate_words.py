def remove_consecutive_duplicates(s: str) -> str:
    if len(s) < 1:
        return ""
    new_word = ""
    s = s.split()
    if len(s) < 1:
        return s[0]
    for x in range(len(s) - 1):
        if s[x] != s[x + 1]:
            new_word += s[x] + " "
    if s[-1] != s[-2]:
        new_word += s[-1]
    return new_word


print(remove_consecutive_duplicates("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))

def remove_consecutive_duplicates2(w):
    results = []
    for word in w.split():
        if word not in results:
            results.append(word)
        elif results[-1] != word:
            results.append(word)
    return " ".join(results)

print(remove_consecutive_duplicates2("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))
