import sys

opcodes = None
i = 0


class Halt(Exception):
    pass


def solve_file(file_path):
    with open(file_path, 'r') as f:
        file_content = f.read()
        solve(file_content)


def solve(inp):
    global opcodes, i
    opcodes = [int(x) for x in inp.split(',')]

    while i < len(opcodes):
        try:
            op, returns, jumps, params, param_modes = parse_opcode(opcodes[i])
            exec_op(op, returns, list(zip(opcodes[i+1: i+1+params], param_modes)))
            if not jumps:
                i += 1 + params
        except Halt:
            return opcodes

    print('Unexpected end')


def parse_opcode(opcode):
    str_op = '{:05}'.format(opcode)
    param_modes = [int(x) for x in str_op[2::-1]]

    if str_op[3:] == '01':
        return lambda x1, x2: x1 + x2, True, False, 3, param_modes
    if str_op[3:] == '02':
        return lambda x1, x2: x1 * x2, True, False, 3, param_modes

    if str_op[3:] == '03':
        return lambda: int(input('Enter: ')), True, False, 1, param_modes
    if str_op[3:] == '04':
        return print, False, False, 1, param_modes

    if str_op[3:] == '05':
        return lambda c, p: jump_if(2, c, p), False, True, 2, param_modes
    if str_op[3:] == '06':
        return lambda c, p: jump_if(2, int(not c), p), False, True, 2, param_modes

    if str_op[3:] == '07':
        return lambda x1, x2: int(x1 < x2), True, False, 3, param_modes
    if str_op[3:] == '08':
        return lambda x1, x2: int(x1 == x2), True, False, 3, param_modes

    if str_op[3:] == '99':
        raise Halt()

    print('Unknown opcode {}'.format(opcode))


def jump_if(params, comp, to_pointer):
    global i
    if comp:
        i = to_pointer
    else:
        i += 1 + params


def exec_op(op, returns, params):
    global opcodes

    vals = [(x if m else opcodes[x]) for x, m in params]
    if returns:
        opcodes[params[-1][0]] = op(*vals[:-1])
    else:
        op(*vals)


if __name__ == '__main__':
    # solve('3,9,8,9,10,9,4,9,99,-1,8')
    # solve('3,3,1107,-1,8,3,4,3,99')
    # solve('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9')
    # solve('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99')
    solve_file(sys.argv[1])

