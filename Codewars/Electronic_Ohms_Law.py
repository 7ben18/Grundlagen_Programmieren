"""
Electronics #1. Ohm's Law
This is based on Ohm's Law: V = IR
being:
V: Voltage in volts (V)
I: Current in amps (A)
R: Resistance in ohms (R)
Task
Create a function ohms_law(s) that has an input string.
Your get a string in the form:
'2R 10V' or '1V 1A' for example.
Each value of magnitude in the string will be expressed in 'V', 'A' or 'R'
Each value is separated by a space bar in the string.
You must return a string with the value of missing magnitude followed by the unit ('V', 'A', 'R').
That value will be rounded to six (6) decimals.
Examples
'2200R 5V' --> '0.002273A'
"""

def Ohms_law(document):
    """
    V: Voltage in volts (V)
    I: Current in amps (A)
    R: Resistance in ohms (R)
    V = IR
    """
    values = document.split()
    for i in values:
        if "A" in i:
            A = int(i[:-1])
        elif "R" in i:
            R = int(i[:-1])
        else:
            V = int(i[:-1])

    if "A" in values and "R" in values:
        return str(A * R) + "V"
    elif "R" in values and "V" in values:
        return str(V / R) + "A"
    elif "A" in values and "V" in values:
        return str(V / A) + "R"

# de kack gaht ned

print(Ohms_law('2200A 5V'))
