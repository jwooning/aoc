import sys
import math
import collections
import itertools
import functools
import struct

import numpy as np

def read_input(path):
    with open(path, 'r') as f:
        return f.read().split('\n')

def parse_input(lines):
    return [l.strip() for l in lines if len(l)]

def run(inp):
    print('p1: {}'.format(p1(inp)))
    print('p2: {}'.format(p2(inp)))

def p1(inp):
    mem = {}
    mask0 = 0
    mask1 = 0
    for l in inp:
        if l.startswith('mask = '):
            mask0, mask1, _ = parse_mask(l[7:])
        elif l.startswith('mem['):
            addr = int(l[4:l.index(']')])
            val = int(l[l.index('=') + 1:])
            mem[addr] = (val & ~mask0) | mask1
        else:
            print(l)
            print('Invalid action')

    return sum(mem.values())

def p2(inp):
    mem = {}
    mask0 = 0
    mask1 = 0
    maskXs = []
    for l in inp:
        if l.startswith('mask = '):
            mask0, mask1, maskXs = parse_mask(l[7:])
        elif l.startswith('mem['):
            addr = int(l[4:l.index(']')])
            val = int(l[l.index('=') + 1:])
            for Xs in itertools.product((0, 1), repeat=len(maskXs)):
                maskX0 = 0
                maskX1 = 0
                for i, maskX in enumerate(Xs):
                    if maskX:
                        maskX1 += maskXs[i]
                    else:
                        maskX0 += maskXs[i]

                mem[(addr & ~maskX0) | maskX1 | mask1] = val
        else:
            print('Invalid action')

    return sum(mem.values())

def parse_mask(mask):
    assert len(mask) == 36
    mask0 = 0
    mask1 = 0
    maskXs = []
    for i in range(0, len(mask)):
        sign = 35 - i
        if mask[i] == '0':
            mask0 += (2 ** sign)
        elif mask[i] == '1':
            mask1 += (2 ** sign)
        elif mask[i] == 'X':
            maskXs.append(2 ** sign)

    return mask0, mask1, maskXs


if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    inp = parse_input(input_)

    run(['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
         'mem[8] = 11',
         'mem[7] = 101',
         'mem[8] = 0'])
    run("""mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".split('\n'))
    run(inp)
