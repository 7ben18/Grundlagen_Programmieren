def read_program():
    # Datei einlesen
    with open("input02_2019") as f:
        mem = [int(x) for x in f.read().split(",")]
    return(mem)

# Input setzen
mem[1], mem[2] = 12, 2


# Programm Interpreter
def run_programm(mem,):
    for i in range(0, len(mem), 4):
        if mem[i] == 99:
            break
        elif mem[i] == 1:
            mem[mem[i+3]] = mem[mem[i+1]] + mem[mem[i+2]]
        elif mem[i] == 2:
            mem[mem[i+3]] = mem[mem[i+1]] * mem[mem[i+2]]
        else:
            raise ValueError

    return(mem[0])


#19690720
#100 * noun + verb

# noun und verb sind zwischen 0 und 99

eis = [i for i in range(0, 100)]
noun = [i for i in range(0,100)]

#print(verb)

for i in eis:
    for x in noun:
        if 19690720 == (100 * x) + i:
            print(i)
