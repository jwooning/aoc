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
    print('p1: {}'.format(simulate(1)))
    print('p2: {}'.format(simulate(2)))

def simulate(dims):
    cycles = 6
    padd = 1
    map_ = np.zeros([x + 2 * (cycles + padd) for x in [len(inp[0]), len(inp)] + [1] * dims], 
                    dtype=np.uint8)
    print(map_.shape)
    z = padd + cycles
    for i in range(len(inp)):
        y = i + padd + cycles
        for j in range(len(inp[i])):
            x = j + padd + cycles

            if inp[i][j] == '#':
                map_[tuple([x, y] + [z] * dims)] = 1

    for i in range(cycles):
        print('{}'.format(np.sum(map_)))
        new_map = map_.copy()
        for pos in itertools.product(*[range(1, size-1) for size in map_.shape]):
            neighbours = map_[tuple([slice(p-1, p+2) for p in pos])]
            assert neighbours.shape == tuple([3] * (dims + 2))
            sum_ = np.sum(neighbours) - map_[pos]
            if map_[pos] == 1 and sum_ != 2 and sum_ != 3:
                new_map[pos] = 0
            elif map_[pos] == 0 and sum_ == 3:
                new_map[pos] = 1
        map_ = new_map

    return np.sum(map_)

if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    inp = parse_input(input_)
    run(['.#.', '..#', '###'])
    run(inp)
