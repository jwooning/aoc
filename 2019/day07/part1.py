import sys
import itertools


def solve_file(file_path):
    with open(file_path, 'r') as f:
        file_content = f.read()
        solve(file_content)


def solve(inp):
    opcodes = [int(x) for x in inp.split(',')]

    r = range(5)
    results = {}
    for phases in itertools.product(r, repeat=5):
        if 0 not in phases or 1 not in phases or 2 not in phases or 3 not in phases or 4 not in phases:
            continue

        ems = []
        for _ in range(5):
            ems.append(IntCodeEmulator(opcodes))

        prev_out = 0
        for i in range(5):
            ems[i].inputs = [phases[i], prev_out]
            ems[i].run()
            prev_out = ems[i].outputs[0]

        results[phases] = prev_out

    print(sorted(results.values(), reverse=True)[0])


class IntCodeEmulator:
    opcodes = None
    i = None
    inputs = None
    outputs = None

    class Halt(Exception):
        pass

    def __init__(self, ops, ins=None):
        self.opcodes = ops
        self.i = 0
        self.inputs = []
        self.outputs = []
        if ins is not None:
            self.inputs = ins

    def run(self):
        while True:
            assert self.i < len(self.opcodes)
            try:
                op, returns, jumps, params, param_modes = self.parse_opcode(self.opcodes[self.i])
                self.exec_op(op, returns, list(zip(self.opcodes[self.i + 1: self.i + 1 + params], param_modes)))
                if not jumps:
                    self.i += 1 + params
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
            return self.outputs.append, False, False, 1, param_modes

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
        assert len(self.inputs)
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
    # solve('3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0')
    solve_file(sys.argv[1])

