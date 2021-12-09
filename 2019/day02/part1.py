import sys
import operator

opcodes = None


def solve_file(file_path):
    with open(file_path, 'r') as f:
        solve(f.read())


def solve(inp):
    global opcodes
    i = 0
    opcodes = [int(x) for x in inp.split(',')]

    # Necessary replacements
    opcodes[1] = 12
    opcodes[2] = 2

    while i < len(opcodes):
        op, params = parse_opcode(opcodes[i])
        exec_op(op, *opcodes[i+1 : i+1+params])
        i += 1 + params
    print(opcodes)


def parse_opcode(opcode):
    if opcode == 1:
        return (operator.add, 3)
    if opcode == 2:
        return (operator.mul, 3)
    elif opcode == 99:
        print('Halt')
        print(opcodes)
        sys.exit()

    print('Unknown opcode {}'.format(opcode))


def exec_op(op, *args):
    global opcodes
    opcodes[args[-1]] = op(*[opcodes[x] for x in args[0:-1]])


if __name__ == '__main__':
    solve_file(sys.argv[1])

