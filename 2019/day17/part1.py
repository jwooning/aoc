class IntCodeEmulator:
    i = None
    rb = None
    _opcodes = None
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
        self.rb = 0
        self._opcodes = ops.copy()
        self.inputs = []
        self.outputs = []
        self.direct = direct

    def run(self):
        while True:
            op, returns, jumps, params, param_modes = self.parse_opcode(self.get_mem(self.i))
            self.exec_op(op, returns, list(zip(self.get_mem(self.i + 1, self.i + 1 + params), param_modes)))
            if not jumps:
                self.i += 1 + params

    def adjust_mem_size(self, addr):
        while addr >= len(self._opcodes):
            self._opcodes += [0] * len(self._opcodes)

    def set_mem(self, addr, val):
        self.adjust_mem_size(addr)
        self._opcodes[addr] = val

    def get_mem(self, addr, addr_end=None):
        self.adjust_mem_size(addr)
        if addr_end is not None:
            self.adjust_mem_size(addr)
            return self._opcodes[addr: addr_end]
        return self._opcodes[addr]

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

        if str_op[3:] == '09':  # move rb
            return self.add_rb, False, False, 1, param_modes

        if str_op[3:] == '99':
            raise type(self).Halt()

        print('Unknown opcode {}'.format(opcode))

    def add_rb(self, x):
        self.rb += x

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

    def val_mode(self, mode, val, return_addr=False):
        assert 0 <= mode <= 2
        assert not (mode == 1 and return_addr)
        if mode == 0:  # positional mode
            return val if return_addr else self.get_mem(val)
        if mode == 1:  # direct mode
            return val
        if mode == 2:  # relative mode
            return self.rb + val if return_addr else self.get_mem(self.rb + val)

    def exec_op(self, op, returns, params):
        vals = [self.val_mode(m, x) for x, m in params]
        if returns:
            self.set_mem(self.val_mode(params[-1][1], params[-1][0], True), op(*vals[:-1]))
        else:
            op(*vals)



def solve_input():
    with open('input', 'r') as f:
        file_content = f.read().strip()
        solve(file_content)


def solve(inp):
    opcodes = [int(x) for x in inp.split(',')]
    icem = IntCodeEmulator(opcodes)

    MAP = [[]]

    while True:
        try:
            icem.run()
        except IntCodeEmulator.Halt:
            pass
        except IntCodeEmulator.InputRequired:
            pass

        while len(icem.outputs):
            ch = chr(icem.outputs.pop(0))
            if ch == '\n':
                MAP.append([])
            else:
                MAP[-1].append(ch)

        while len(MAP[-1]) == 0:
            del MAP[-1]

        alignments_sum = 0
        for i in range(1, len(MAP)-1):
            for j in range(1, len(MAP[0])-1):
                if MAP[i][j] == '#':
                    if MAP[i][j+1] == '#' and MAP[i][j-1] == '#' and MAP[i+1][j] == '#' and MAP[i-1][j] == '#':
                        alignments_sum += i * j

        print(alignments_sum)

        break


if __name__ == '__main__':
    solve_input()
