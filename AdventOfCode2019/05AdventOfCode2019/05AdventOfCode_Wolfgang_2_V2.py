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


def add(mem, ic):
    mem[mem[ic + 3]] = get_parameter(mem, ic, 1) + get_parameter(mem, ic, 2)
    return ic + 4


def mul(mem, ic):
    mem[mem[ic + 3]] = get_parameter(mem, ic, 1) * get_parameter(mem, ic, 2)
    return ic + 4


def input_(mem, ic, input_function):
    mem[mem[ic + 1]] = input_function()
    return ic + 2


def output_(mem, ic, output_function):
    output_function(get_parameter(mem, ic, 1))
    return ic + 2


def jmp_true(mem, ic):
    return get_parameter(mem, ic, 2) if get_parameter(mem, ic, 1) != 0 else ic + 3


def jmp_false(mem, ic):
    return get_parameter(mem, ic, 2) if get_parameter(mem, ic, 1) == 0 else ic + 3


def less(mem, ic):
    mem[mem[ic + 3]] = 1 if get_parameter(mem, ic, 1) < get_parameter(mem, ic, 2) else 0
    return ic + 4


def equals(mem, ic):
    mem[mem[ic + 3]] = 1 if get_parameter(mem, ic, 1) == get_parameter(mem, ic, 2) else 0
    return ic + 4


def run_program(mem, input_function, output_function):
    # Programm interpreter
    ic = 0
    while ic < len(mem) and mem[ic] != 99:
        op_code = get_op_code(mem[ic])
        if op_code == 1:
            ic = add(mem, ic)
        elif op_code == 2:
            ic = mul(mem, ic)
        elif op_code == 3:  # input
            ic = input_(mem, ic, input_function)
        elif op_code == 4:  # output
            ic = output_(mem, ic, output_function)
        elif op_code == 5:  # jmp if true
            ic = jmp_true(mem, ic)
        elif op_code == 6:  # jmp if false
            ic = jmp_false(mem, ic)
        elif op_code == 7:  # less than
            ic = less(mem, ic)
        elif op_code == 8:  # less than
            ic = equals(mem, ic)
        else:
            raise ValueError
    return mem[0]


def input_value():
    return 5


run_program(read_program('input_aoc_19_05.txt'), input_value, print)
