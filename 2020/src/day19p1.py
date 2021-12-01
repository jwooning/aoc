import sys
import math
import collections
import itertools
import functools
import struct
import copy

import numpy as np

def read_input(path):
    with open(path, 'r') as f:
        return f.read().split('\n')

def parse_input(lines):
    return [l.strip() for l in lines if len(l)]

def run(inp):
    rules = {}

    # Parse rules
    for i, line in enumerate(inp):
        if ':' not in line:
            break

        num, rule = line.split(': ')
        num = int(num)
        rules[num] = [None, []]
        for subrule in rule.split(' | '):
            if subrule[0] == '"':
                rules[num] = [1, subrule[1:-1]]
                break

            rules[num][1].append([int(x) for x in subrule.split(' ')])

    find_lens(rules)

    for num, val in rules.items():
        if num in [0, 8, 11, 31, 42]:
            print(num, val)

    p1 = 0
    for line in inp[i:]:
        if evaluate(rules, 0, line, 0):
            p1 += 1

    print('p1: {}'.format(p1))

def find_lens(rules):
    queue = collections.deque([0])
    while len(queue):
        num = queue.popleft()
        if rules[num][0] is not None:
            continue

        lens = [0] * len(rules[num][1])
        valid = True
        for j, subrule in enumerate(rules[num][1]):
            for subnum in subrule:
                if rules[subnum][0] is None:
                    queue.appendleft(subnum)
                    valid = False
                else:
                    lens[j] += rules[subnum][0]

        if valid:
            for len_ in lens:
                if len_ != lens[0]:
                    print(':(')
                    return

            rules[num][0] = lens[0]
        else:
            queue.append(num)

def evaluate(rules, num, line, nest):
    len_, rule = rules[num]
    if len_ != len(line):
        return False

    if type(rule) == str:
        assert len_ == 1
        return line == rule

    for subrule in rule:
        i = 0
        valid = True
        for subnum in subrule:
            len_ = rules[subnum][0]

            if not evaluate(rules, subnum, line[i:i+len_], nest+1):
                valid = False
                break

            i += len_

        if valid:
            return True

    return False


if __name__ == '__main__':
    input_ = read_input('input/day19')
    inp = parse_input(input_)
    run("""0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"
ababbb
bababa
abbbab
aaabbb
aaaabbb""".split('\n'))
    run(inp)
