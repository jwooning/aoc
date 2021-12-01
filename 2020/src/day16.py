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
    classes = []
    for i in range(0, len(inp)):
        line = inp[i]
        if line == 'your ticket:':
            break

        class_, ranges_s = line.split(': ')
        ranges = []
        for ran in ranges_s.split(' or '):
            x0, x1 = ran.split('-')
            ranges.append((int(x0), int(x1)))
        
        classes.append((class_, ranges))

    my_ticket = [int(x) for x in inp[i+1].split(',')]
    other_tickets = []
    for i in range(i+3, len(inp)):
        other_tickets.append([int(x) for x in inp[i].split(',')])

    valid_tickets = []
    p1 = 0
    for ticket in other_tickets:
        valid_ticket = True
        for val in ticket:
            valid = False
            for cls, ranges in classes:
                if valid:
                    break
                for rang in ranges:
                    if rang[0] <= val and val <= rang[1]:
                        valid = True
                        break

            if not valid:
                p1 += val
                valid_ticket = False

        if valid_ticket:
            valid_tickets.append(ticket)

    print('p1: {}'.format(p1))

    valid_map = np.zeros((len(classes), len(valid_tickets[0])), dtype=np.uint8)
    j = 0
    for cls, ranges in classes:
        for i in range(0, len(valid_tickets[0])):
            valid_index = True
            for ticket in valid_tickets:
                in_range = False
                for x0, x1 in ranges:
                    if x0 <= ticket[i] and ticket[i] <= x1:
                        in_range = True
                        break

                if not in_range:
                    valid_index = False
                    break

            if valid_index:
                valid_map[j, i] = 1

        j += 1

    print(valid_map)
    class_map = {}
    while len(class_map) < len(classes):
        for i in range(0, len(classes)):
            if np.sum(valid_map[:, i]) == 1:
                cls_index = np.where(valid_map[:, i] == 1)[0][0]
                class_map[classes[cls_index][0]] = i
                valid_map[cls_index, :] = 0
                break

    print(class_map)

    p2 = 1
    for cls, index in class_map.items():
        if cls.startswith('departure'):
            p2 *= my_ticket[index]

    print('p2: {}'.format(p2))

if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    inp = parse_input(input_)
    run("""class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19
your ticket:
11,12,13
nearby tickets:
3,9,18
15,1,5
5,14,9""".split('\n'))
    run(inp)
