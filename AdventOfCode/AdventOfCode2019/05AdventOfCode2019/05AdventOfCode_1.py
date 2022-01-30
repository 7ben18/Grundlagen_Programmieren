
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

def run_program(liste, input_function, output_function):
    ic = 0
    while ic < len(liste) and liste[ic] != 99:
        if liste[ic] == 1:
            liste[liste[ic + 3]] = liste[liste[ic + 1]] + liste[liste[ic + 2]]
            ic += 4
        elif liste[ic] == 2:
            liste[liste[ic + 3]] = liste[liste[ic + 1]] * liste[liste[ic + 2]]
            ic += 4
        elif liste[ic] == 3:
            liste[liste[ic + 1]] = input_function()
            ic += 2
        elif liste[ic] == 4:
            output_function(liste[liste[ic + 1]])
            ic += 2
        else:
            raise ValueError
    return liste[0]

def input_value():
    return 212

run_program([3,0,4,0,99], input_value, print)