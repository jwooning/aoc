import sys
import itertools


def solve_file(file_path):
    with open(file_path, 'r') as f:
        file_content = f.read()
        solve(file_content)


def solve(inp):
    opcodes = [int(x) for x in inp.split(',')]

    r = range(5, 10)
    results = {}
    for phases in itertools.product(r, repeat=5):
        if len(set(phases)) != len(phases):  # continue on duplicates
            continue

        results[phases] = calc_out(opcodes, phases)

    print(sorted(results.values(), reverse=True)[0])


def calc_out(opcodes, phases):
    ems = []
    for i in range(5):
        ems.append(IntCodeEmulator(opcodes))
        ems[i].inputs.append(phases[i])

    prev_out = [0]
    i = 0
    while True:
        ems[i].inputs += prev_out
        ems[i].run()

        prev_out = ems[i].outputs
        ems[i].outputs = []

        if i == 4 and not ems[i].paused:
            break
        i = (i + 1) % 5

    assert len(prev_out) == 1
    return prev_out[0]


class IntCodeEmulator:
    i = None
    opcodes = None
    inputs = None
    outputs = None
    paused = None
    direct = None

    class Halt(Exception):
        pass

    class InputRequired(Exception):
        pass

    def __init__(self, ops, direct=False):
        self.i = 0
        self.opcodes = ops.copy()
        self.inputs = []
        self.outputs = []
        self.paused = False
        self.direct = direct

    def run(self):
        self.paused = False
        while not self.paused:
            assert self.i < len(self.opcodes)
            try:
                op, returns, jumps, params, param_modes = self.parse_opcode(self.opcodes[self.i])
                self.exec_op(op, returns, list(zip(self.opcodes[self.i + 1: self.i + 1 + params], param_modes)))
                if not jumps:
                    self.i += 1 + params
            except type(self).InputRequired:
                self.paused = True
            except type(self).Halt:
                return self.opcodes

    def parse_opcode(self, opcode):
        str_op = '{:05}'.format(opcode)
        param_modes = [int(x) for x in str_op[2::-1]]

        if str_op[3:] == '01':  # add
            return lambda x1, x2: x1 + x2, True, False, 3, param_modes
        if str_op[3:] == '02':  # mult
            return lambda x1, x2: x1 * x2, True, False, 3, param_modes

        if str_op[3:] == '03':  # input
            return self.input, True, False, 1, param_modes
        if str_op[3:] == '04':  # output
            return (print if self.direct else self.outputs.append), False, False, 1, param_modes

        if str_op[3:] == '05':  # jump if 1
            return lambda c, p: self.jump_if(2, c, p), False, True, 2, param_modes
        if str_op[3:] == '06':  # jump if 0
            return lambda c, p: self.jump_if(2, int(not c), p), False, True, 2, param_modes

        if str_op[3:] == '07':  # le
            return lambda x1, x2: int(x1 < x2), True, False, 3, param_modes
        if str_op[3:] == '08':  # eq
            return lambda x1, x2: int(x1 == x2), True, False, 3, param_modes

        if str_op[3:] == '99':
            raise type(self).Halt()

        print('Unknown opcode {}'.format(opcode))

    def input(self):
        if self.direct:
            return int(input('Enter: '))

        if not len(self.inputs):
            raise type(self).InputRequired()

        return self.inputs.pop(0)

    def jump_if(self, params, comp, to_pointer):
        if comp:
            self.i = to_pointer
        else:
            self.i += 1 + params

    def exec_op(self, op, returns, params):
        vals = [(x if m else self.opcodes[x]) for x, m in params]
        if returns:
            self.opcodes[params[-1][0]] = op(*vals[:-1])
        else:
            op(*vals)


if __name__ == '__main__':
    # print(calc_out([3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5], (9,8,7,6,5)))

    solve_file(sys.argv[1])

