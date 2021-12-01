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
                rules[num] = [[1, False], subrule[1:-1]]
                break

            rules[num][1].append([int(x) for x in subrule.split(' ')])

    rules[8] = [[8, True], [[42], [42, 8]]]
    rules[11] = [[16, True], [[42, 31], [42, 11, 31]]]

    find_lens(rules)

    for num, val in rules.items():
        len_, rule = val
        if num in [0, 8, 11, 31, 42]:
            print(num, len_, rule)

    p2 = 0
    inval = []
    for j, line in enumerate(inp[i:]):
        res = evaluate(rules, 0, line, 0)
        if res:
            p2 += 1
        else:
            inval.append(j)

    print(inval)
    print('p2: {}'.format(p2))

def find_lens(rules):
    queue = collections.deque([0, 42, 31])
    while len(queue):
        num = queue.popleft()
        if rules[num][0] is not None:
            continue

        lens = []
        for _ in range(len(rules[num][1])):
            lens.append([0, False])

        valid = True
        for j, subrule in enumerate(rules[num][1]):
            for subnum in subrule:
                if rules[subnum][0] is None:
                    queue.appendleft(subnum)
                    valid = False
                else:
                    lens[j][0] += rules[subnum][0][0]
                    lens[j][1] = bool(lens[j][1] + rules[subnum][0][1])

        if valid:
            rules[num][0] = lens[0]
        else:
            queue.append(num)

def evaluate(rules, num, line, nest):
    if num in [0, 8, 11, 31, 42]:
        print('|' * nest, num, line, len(line))
    len42 = 8
    len_, rule = rules[num]
    if type(rule) == str:
        return line == rule

    if not len_[1] and len_[0] != len(line):
        print('|' * nest, 'static len')
        return False

    if num == 8:
        if len(line) < len42 or len(line) % len42 != 0:
            print('|' * nest, 'dyn len')
            return False
        rule = [[42] * (len(line) // len42)]
    elif num == 11:
        if len(line) < (len42 * 2) or len(line) % (len42 * 2) != 0:
            print('|' * nest, 'dyn len')
            return False
        times = len(line) // (len42 * 2)
        rule = [[42] * times + [31] * times]
    elif num == 0:
        if len(line) < (len42 * 3) or len(line) % len42 != 0:
            return False
        
        for i in range(len42, len(line) - (len42 * 2) + 1, len42):
            if evaluate(rules, 8, line[:i], nest+1) and evaluate(rules, 11, line[i:], nest+1):
                print('|' * nest, 'num 0 found, i = {}'.format(i))
                return True
        print('|' * nest, 'num 0 exhausted')
        return False


    if num in [0, 8, 11, 31, 42]:
        print('|' * nest, 'rule', rule)
    for subrule in rule:
        i = 0
        valid = True
        for subnum in subrule:
            len_ = rules[subnum][0][0]

            if not evaluate(rules, subnum, line[i:i+len_], nest+1):
                valid = False
                break

            i += len_

        if valid:
            if num in [8, 11, 31, 42]:
                print('|' * nest, 'static found')
            return True

    if num in [8, 11, 31, 42]:
        print('|' * nest, 'static exhausted')
    return False


if __name__ == '__main__':
    input_ = read_input('input/day19')
    inp = parse_input(input_)
    run("""42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1
abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba""".split('\n'))
    run(inp)
