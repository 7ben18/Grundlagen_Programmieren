
"""
Opcode
1 = Addition
2 = Multiplikation
3 = Input Value wird an Position X gespeichert (3,X)
4 = Output Value wird an Position X gespeichert (4,X)

Position Mode = Bezieht sich auf den Wert in dieser Position
Immediate Mode = Der Tatsaechliche Wert.

1002,4,3,4,33 -> 01002,4,3,4,99

ABCDE
01002

02 = Opcode = Multiplikation
1 Zahl nach dem Code = 4, 0 = Position Mode
2 Zahl nach dem Code = 3, 1 = Immediate Mode
3 Zahl nach dem Code = 4, 0 = Position Mode
"""

def einlesen_liste(daten):
    with open(daten) as f:
        return (list(map(int, f.readline().split(","))))

input = einlesen_liste("05data")
print(input) #[3,255,1......]

