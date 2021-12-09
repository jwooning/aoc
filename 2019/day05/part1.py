import sys
import operator

opcodes = None


class Halt(Exception):
    pass


def solve_file(file_path):
    with open(file_path, 'r') as f:
        file_content = f.read()
        solve(file_content)


def solve(inp):
    global opcodes
    i = 0
    opcodes = [int(x) for x in inp.split(',')]

    while i < len(opcodes):
        try:
            op, returns, params, param_modes = parse_opcode(opcodes[i])
            exec_op(op, returns, list(zip(opcodes[i+1: i+1+params], param_modes)))
            i += 1 + params
        except Halt:
            return opcodes[0]

    print('Unexpected end')


def parse_opcode(opcode):
    str_op = '{:05}'.format(opcode)
    param_modes = [int(x) for x in str_op[2::-1]]

    if str_op[3:] == '01':
        return operator.add, True, 3, param_modes
    if str_op[3:] == '02':
        return operator.mul, True, 3, param_modes
    if str_op[3:] == '03':
        return input_int, True, 1, param_modes
    if str_op[3:] == '04':
        return print, False, 1, param_modes
    if str_op[3:] == '99':
        raise Halt()

    print('Unknown opcode {}'.format(opcode))


def input_int():
    return int(input('Enter: '))


def exec_op(op, returns, params):
    global opcodes

    vals = [(x if m else opcodes[x]) for x, m in params]
    if returns:
        opcodes[params[-1][0]] = op(*vals[:-1])
    else:
        op(*vals)


if __name__ == '__main__':
    # solve('3,0,4,0,99')
    # solve('1002,4,3,4,33')
    solve_file(sys.argv[1])

