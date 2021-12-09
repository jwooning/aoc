import numpy as np
from matplotlib import pyplot as plt


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


DIRS_OUT = {
    0: 1,
    1: 3,
    2: 2,
    3: 4,
}
DIRS_DELTA = {
    0: ( 0, -1),
    1: (-1,  0),
    2: ( 0,  1),
    3: ( 1,  0),
}
MAP = np.empty(shape=(41, 41), dtype=np.int8)  # -1: unknown, 0: wall, 1: space, 2: oxygen
MAP.fill(-1)


def solve_input():
    with open('input', 'r') as f:
        file_content = f.read().strip()
        solve(file_content)


def solve(inp):
    global MAP
    opcodes = [int(x) for x in inp.split(',')]
    icem = IntCodeEmulator(opcodes)

    start_x, start_y = 21, 21
    x, y = start_x, start_y
    dir = 0
    MAP[x, y] = 1

    icem.inputs.append(DIRS_OUT[dir])
    while True:
        try:
            icem.run()
        except IntCodeEmulator.InputRequired:
            pass
        except KeyboardInterrupt:
            break

        out = icem.outputs.pop(0)

        new_x = x + DIRS_DELTA[dir][0]
        new_y = y + DIRS_DELTA[dir][1]
        MAP[new_x, new_y] = out

        if out > 0:
            x, y = new_x, new_y

            if x == start_x and y == start_y and np.any(MAP == 2):
                break

        try:
            right_dir = (dir + 1) % 4
            left_dir = (dir - 1) % 4
            if MAP[x + DIRS_DELTA[right_dir][0], y + DIRS_DELTA[right_dir][1]] != 0:
                dir = right_dir
            elif MAP[x + DIRS_DELTA[dir][0], y + DIRS_DELTA[dir][1]] != 0:
                pass
            elif MAP[x + DIRS_DELTA[left_dir][0], y + DIRS_DELTA[left_dir][1]] != 0:
                dir = left_dir
            else:
                dir = (dir + 2) % 4  # Turn around

            icem.inputs.append(DIRS_OUT[dir])
        except:
            break

    MAP[start_x, start_y] = 3

    plt.imshow(MAP)
    plt.show()

    solve_dist(21, 21, 3, 0)
    solve_flow()


def solve_dist(x, y, dir, steps):
    if MAP[x, y] == 2:
        print('FOUND ROUTE {}'.format(steps))
        return

    for d_dir in [-1, 0, 1]:
        new_dir = (dir + d_dir) % 4
        new_x = x + DIRS_DELTA[new_dir][0]
        new_y = y + DIRS_DELTA[new_dir][1]
        if MAP[new_x, new_y] > 0:
            solve_dist(new_x, new_y, new_dir, steps + 1)


def solve_flow():
    global MAP
    MAP[21, 21] = 1
    mins = 0
    while np.any(MAP == 1):
        NEW_MAP = MAP.copy()
        for i in range(MAP.shape[0]):
            for j in range(MAP.shape[1]):
                if MAP[i, j] == 1:
                    if MAP[i + 1, j] == 2 or MAP[i - 1, j] == 2 or MAP[i, j + 1] == 2 or MAP[i, j - 1] == 2:
                        NEW_MAP[i, j] = 2

        MAP = NEW_MAP
        mins += 1

    print('MIN TO FILL {}'.format(mins))




if __name__ == '__main__':
    solve_input()
