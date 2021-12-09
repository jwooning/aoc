import numpy as np
from matplotlib import pyplot as plt

from day11.part2 import IntCodeEmulator


def solve_input():
    with open('input', 'r') as f:
        file_content = f.read().strip()
        solve(file_content)


def solve(inp):
    screen = np.zeros((0, 0), dtype=np.uint8)
    opcodes = [int(x) for x in inp.split(',')]
    icem = IntCodeEmulator(opcodes)
    icem.set_mem(0, 2)
    while True:
        try:
            icem.run()
        except IntCodeEmulator.Halt:
            print('HALT')
            break
        except IntCodeEmulator.InputRequired:
            pass

        while icem.outputs:
            x, y, id = icem.outputs.pop(0), icem.outputs.pop(0), icem.outputs.pop(0)
            if x == -1 and y == 0:
                print('SCORE: {}'.format(id))
            else:
                if x >= screen.shape[1] - 1:
                    screen = np.c_[screen, np.zeros(shape=(screen.shape[0], 1), dtype=np.uint8)]
                if y >= screen.shape[0] - 1:
                    screen = np.r_[screen, np.zeros(shape=(1, screen.shape[1]), dtype=np.uint8)]

                screen[y, x] = id

        plt.imshow(screen)
        plt.show()


if __name__ == '__main__':
    solve_input()
