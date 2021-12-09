import sys
import operator

opcodes = None


class Halt(Exception):
    pass


def solve_file(file_path):
    with open(file_path, 'r') as f:
        file_content = f.read()
        for i in range(0, 100):
            for j in range(0, 100):
                res = solve(file_content, i, j)
                if res == 19690720:
                    print(i, j, 100 * i + j)
                    return


def solve(inp, noun, verb):
    global opcodes
    i = 0
    opcodes = [int(x) for x in inp.split(',')]

    # Necessary replacements
    opcodes[1] = noun
    opcodes[2] = verb

    while i < len(opcodes):
        try:
            op, params = parse_opcode(opcodes[i])
            exec_op(op, *opcodes[i+1 : i+1+params])
            i += 1 + params
        except Halt:
            return opcodes[0]

    print('Unexpected end')


def parse_opcode(opcode):
    if opcode == 1:
        return (operator.add, 3)
    if opcode == 2:
        return (operator.mul, 3)
    elif opcode == 99:
        raise Halt()

    print('Unknown opcode {}'.format(opcode))


def exec_op(op, *args):
    global opcodes
    opcodes[args[-1]] = op(*[opcodes[x] for x in args[0:-1]])


if __name__ == '__main__':
    solve_file(sys.argv[1])

