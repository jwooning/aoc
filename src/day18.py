import sys
import math
import collections
import itertools
import functools
import struct

import numpy as np

def str_index(str_, chars):
    for i, ch in enumerate(str_):
        if ch in chars:
            return i
    return len(str_)

def read_input(path):
    with open(path, 'r') as f:
        return f.read().split('\n')

def parse_input(lines):
    return [l.strip() for l in lines if len(l)]

def run(inp):
    p1 = 0
    p2 = 0
    for line in inp:
        ast1 = parse(line, lambda l: find_op(l, list('*+')))
        p1 += evaluate(ast1)
        ast2 = parse(line, find_op_precedence)
        p2 += evaluate(ast2)
    print('p1: {}'.format(p1))
    print('p2: {}'.format(p2))

def find_op_precedence(line):
    first_op = find_op(line, ['*'])
    if first_op is not None:
        return first_op

    return find_op(line, ['+'])

def find_op(line, ops):
    nest = 0
    for i in range(len(line)-1, -1, -1):
        ch = line[i]
        if nest == 0 and ch in ops:
            return i

        if ch == '(':
            nest += 1
        elif ch == ')':
            nest -= 1

    return None

def parse(line, opi):
    line = line.replace(' ', '')

    first_op = opi(line)
    if first_op is not None:  # Line contains a top-level operator
        return line[first_op], parse(line[:first_op], opi), parse(line[first_op+1:], opi)
    elif line[0] == '(':  # line is expression in parentheses
        return parse(line[1:-1], opi)
    else:  # Line is a number
        return int(line)

def evaluate(ast):
    if type(ast) == tuple:
        op, e0, e1 = ast
        if op == '+':
            return evaluate(e0) + evaluate(e1)
        if op == '*':
            return evaluate(e0) * evaluate(e1)

    return ast


if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    inp = parse_input(input_)
    run(['1 + 2 * 3 + 4 * 5 + 6'])
    run(['1 + (2 * 3) + (4 * (5 + 6))'])
    run(inp)
