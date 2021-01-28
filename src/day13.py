import sys
import math
import collections
import itertools
import functools

import numpy as np

def lcm(a, b):
    return a * b // math.gcd(a, b)

def lcmm(*args):
    return functools.reduce(lcm, args)

def gcdd(*args):
    return functools.reduce(math.gcd, args)

def read_input(path):
    with open(path, 'r') as f:
        return f.read().split('\n')

def parse_input(lines):
    return [l for l in lines if len(l)]

def run(inp):
    earliest = int(inp[0])
    busses = [(0 if x == 'x' else int(x)) for x in inp[1].split(',')]
    
    min_wait = float('Inf')
    min_bus = None
    for bus in busses:
        if bus == 0:
            continue

        wait = bus - (earliest % bus)
        if wait < min_wait:
            min_wait = wait
            min_bus = bus
    print('p1: {}'.format(min_wait * min_bus))

    bus_i = [(bus, i) for i, bus in enumerate(busses) if bus != 0]
    prev_res = 0
    for j in range(1, len(bus_i)):
        lcm = lcmm(*[bus for bus, i in bus_i[:j]])
        print(prev_res, lcm)
        bus, i = bus_i[j]
        t = prev_res
        while True:
            t += lcm
            if (t + i) % bus == 0:
                break

        print('(t - prev_res) / lcm = {}'.format((t - prev_res)/lcm))

        prev_res = t

    print('p2: {}'.format(prev_res))

if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    inp = parse_input(input_)
    run(['939', '7,13,x,x,59,x,31,19'])
    print('---')
    run(['0', '1789,37,47,1889'])
    print('---')
    run(inp)
