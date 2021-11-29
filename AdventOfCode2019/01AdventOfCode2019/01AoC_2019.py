def einlesen():
    with open("01AoC2019") as f:
        return [int(x) for x in f.read().split("\n")]

#def rechnung(l = list) -> int:
def rechnung(l) -> int:
    return sum([((x // 3) - 2) for x in l])

#print(rechnung(einlesen()))

def run2(l) -> int:
    summe = 0
    for a in l:
        while a >= 6:
            a = a // 3 - 2
            summe += a
    return summe

print(run2(einlesen()))