import sys

import collections
import itertools


def read_input(path):
    with open(path, 'r') as f:
        for line in f:
            yield line[:-1]


def run(lines):
    code = [int(x) for x in lines]
    p1 = None

    for i in range(25, len(code)):
        valid = False
        for a, b in itertools.combinations(code[i - 25: i], r=2):
            if code[i] == (a + b):
                valid = True
                break

        if not valid:
            p1 = code[i]
            break

    print('p1: {}'.format(p1))

    for i in range(0, len(code)):
        k = []
        for j in range(i, len(code)):
            k.append(code[j])
            if sum(k) == p1:
                print('p2: {}'.format(min(k) + max(k)))
                return
            elif sum(k) > p1:
                break

if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    run(input_)
