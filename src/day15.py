import sys
import math
import collections
import itertools
import functools
import struct

import numpy as np

def run(inp, amount):
    print('p2: {}'.format(p2(inp, amount)))
    print('p1: {}'.format(p1(inp, amount)))

def p1(inp, amount):
    spoken = inp + ([0] * amount)
    for i in range(len(inp), amount):
        try:
            indx = spoken[i-2::-1].index(spoken[i-1])
            spoken[i] = indx + 1
        except ValueError:
            spoken[i] = 0

    return spoken[i]

def p2(inp, amount):
    spoken = {x: i for i, x in enumerate(inp[:-1])}
    prev = inp[-1]
    for i in range(len(inp), amount):
        try:
            new = i - spoken[prev] - 1
        except KeyError:
            new = 0

        spoken[prev] = i - 1
        prev = new

    return prev

if __name__ == '__main__':
    run([0,3,6], 10)
    run([11,0,1,10,5,19], 2020)
    run([11,0,1,10,5,19], 30000000)

