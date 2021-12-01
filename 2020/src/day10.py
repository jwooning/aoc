import sys

import collections
import itertools


t0 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]

def read_input(path):
    with open(path, 'r') as f:
        for line in f:
            yield line[:-1]

def parse_input(lines):
    return [int(x) for x in lines]

def run(inp):
    inp = [0] + sorted(inp)
    inp.append(inp[-1] + 3)

    d1 = 0
    d3 = 0
    for i in range(1, len(inp)):
        d = inp[i] - inp[i - 1]
        if d == 1:
            d1 += 1
        elif d == 3:
            d3 += 1

    print('p1: {} {}'.format(d1 * d3, (d1, d3)))

    poss = {0: 1}
    for i in range(1, len(inp)):
        res = 0
        for j in range(i - 3, i):
            if j >= 0 and inp[j] + 3 >= inp[i]:
                res += poss[j]
        poss[i] = res

    print('p2: {}'.format(poss[len(inp)-1]))


if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    inp = parse_input(input_)
    run(t0)
    run(inp)
