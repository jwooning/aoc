import sys

import collections
import itertools
import functools

import numpy as np

def turn_left(x, y):
    return [-y, x]

def turn_right(x, y):
    return [y, -x]

def read_input(path):
    with open(path, 'r') as f:
        return f.read().split('\n')

def parse_input(lines):
    return [l for l in lines if len(l)]

def run(inp):
    print('p1: {}'.format(sum([abs(x) for x in navigate(inp)])))
    print('p2: {}'.format(sum([abs(x) for x in navigate_p2(inp)])))

def navigate(inp):
    direction = (1, 0)
    pos = [0, 0]
    for l in inp:
        action = l[0]
        amount = int(l[1:])
        if action == 'N':
                pos[1] += amount
        elif action == 'S':
                pos[1] -= amount
        elif action == 'E':
                pos[0] += amount
        elif action == 'W':
                pos[0] -= amount
        elif action == 'L':
            assert amount % 90 == 0
            for _ in range(0, amount, 90):
                direction = turn_left(*direction)
        elif action == 'R':
            assert amount % 90 == 0
            for _ in range(0, amount, 90):
                direction = turn_right(*direction)
        elif action == 'F':
            pos[0] += amount * direction[0]
            pos[1] += amount * direction[1]

    return pos

def navigate_p2(inp):
    wp = [10, 1]
    pos = [0, 0]
    for l in inp:
        action = l[0]
        amount = int(l[1:])
        if action == 'N':
            wp[1] += amount
        elif action == 'S':
            wp[1] -= amount
        elif action == 'E':
            wp[0] += amount
        elif action == 'W':
            wp[0] -= amount
        elif action == 'L':
            assert amount % 90 == 0
            for _ in range(0, amount, 90):
                wp = turn_left(*wp)
        elif action == 'R':
            assert amount % 90 == 0
            for _ in range(0, amount, 90):
                wp = turn_right(*wp)
        elif action == 'F':
            pos[0] += amount * wp[0]
            pos[1] += amount * wp[1]

    return pos

if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    inp = parse_input(input_)

    t0 = """F10
N3
F7
R90
F11"""
    run(t0.split('\n'))
    run(inp)
