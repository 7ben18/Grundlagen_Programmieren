"""
T1 = 0 (Startwert)
T2 = 3 (Startwert)
T3 = 6 (Startwert)

T4 = 0 (Weil 6 neu ist)
T5 = 4 (von T4) - 1 (von T1) = 3
T6 = 5 (von T5) - 2 (von T2) = 3
T7 = 1 (Weil 3, 2 x hintereinander vorkam)
T8 = 0 (Weil 1 neu ist)
T9 = 8 (von T8) - 4 (von T1) = 4
T10 = 0 (Weil 4 neu ist)

Spiel wird so lange gespielt bis zum T2020
"""
def twicenums(list):
    if list[-1] in list[:-1]:
        num = list.index(list[-1]) - list.index(list[-1])
        return list.append(num)

def startnums(list):
    return list

def uniquenumber(list):
    if list[-1] not in list[:-1]:
        return list.append(0)
    else:
        return False
