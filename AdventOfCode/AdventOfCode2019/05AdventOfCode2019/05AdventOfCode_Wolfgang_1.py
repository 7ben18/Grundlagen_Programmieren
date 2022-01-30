def read_program(file_name):
    # Datei einlesen: Datei in mem: list[int]
    with open(file_name) as f:
        return [int(x) for x in f.read().split(',')]


def get_op_code(instruction: int) -> int:
    return instruction % 100


def get_parameter_mode(instruction: int, para_num: int) -> int:
    return (instruction // 10 ** (para_num + 1)) % 10


def get_parameter(mem, ic, para_num):
    return mem[mem[ic + para_num]] if get_parameter_mode(mem[ic], para_num) == 0 else mem[ic + para_num]


def run_program(mem, input_function, output_function):
    # Programm interpreter
    ic = 0
    while ic < len(mem) and mem[ic] != 99:
        instr = get_op_code(mem[ic])
        if instr == 1:
            mem[mem[ic + 3]] = get_parameter(mem, ic, 1) + get_parameter(mem, ic, 2)
            ic += 4
        elif instr == 2:
            mem[mem[ic + 3]] = get_parameter(mem, ic, 1) * get_parameter(mem, ic, 2)
            ic += 4
        elif instr == 3:  # input
            mem[mem[ic + 1]] = input_function()
            ic += 2
        elif instr == 4:  # output
            output_function(get_parameter(mem, ic, 1))
            ic += 2
        else:
            raise ValueError
    return mem[0]


def input_value():
    return 1


run_program(read_program('05data'), input_value, print)
