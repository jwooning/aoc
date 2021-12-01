import sys
import math
import collections
import itertools
import functools
import struct
import time

import numpy as np

def read_input(path):
    with open(path, 'r') as f:
        return f.read().split('\n')

def parse_input(lines):
    return [l.strip() for l in lines if len(l)]

def run(card_pub, door_pub):
    card_loops = transform_find(7, card_pub)
    door_loops = transform_find(7, door_pub)
    assert transform(7, card_loops) == card_pub
    assert transform(7, door_loops) == door_pub

    card_key = transform(door_pub, card_loops)
    door_key = transform(card_pub, door_loops)
    print(card_key, door_key)
    assert card_key == door_key

    print('p1: {}'.format(card_key))

def transform(sub, loops):
    val = 1
    for _ in range(loops):
        val = (val * sub) % 20201227
    return val

def transform_find(sub, val):
    i = 0
    while val != 1:
        while val % sub != 0:
            val += 20201227
        val = val // sub
        i += 1
    print(sub, i, val)
    return i

def find_loops(vals):
    i = 0
    while True:
        val = transform(7, i)
        if val in vals:
            print(i, val)
        i += 1

if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    card_pub, door_pub = [int(x) for x in parse_input(input_)]
    run(card_pub, door_pub)

