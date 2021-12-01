import sys
import math
import collections
import itertools
import functools
import struct
import time

import numpy as np

class Cycle:
    def __init__(self, lst):
        self.curr = None
        self.cups = {}
        prev = None
        for c in lst:
            node = [c, prev, None]
            self.cups[c] = node
            if self.curr is None:
                self.curr = node
            if prev is not None:
                prev[2] = node
            prev = node
        prev[2] = self.curr
        self.curr[1] = prev

    def cycle(self):
        res = self.curr[0]
        self.curr = self.curr[2]
        return res

    def cycle_until(self, dst):
        while self.curr[0] != dst:
            self.curr = self.curr[2]

    def pop(self):
        res = self.curr[0]
        self.curr[1][2] = self.curr[2]
        self.curr[2][1] = self.curr[1]
        self.curr = self.curr[2]
        return res

    def remove3(self):
        res = self.curr
        self.curr[1][2] = self.curr[2][2][2]
        self.curr[2][2][2][1] = self.curr[1]
        self.curr = self.curr[2][2][2]
        res[1] = None
        res[2][2][2] = None
        return res, [res[0], res[2][0], res[2][2][0]]

    def insert_at(self, dst, node):
        f = self.cups[dst]
        nxt = f[2]

        f[2] = node
        node[1] = f

        node[2][2][2] = nxt
        nxt[1] = node[2][2]

    def __str__(self):
        lst = []
        f = self.curr
        while True:
            lst.append(f[0])
            f = f[2]
            if f == self.curr:
                break
        return str(lst)

def nslice(lst, i, c):
    n = len(lst)
    i = i % n
    if i + c <= n:
        return lst[i: i + c]
    return lst[i:] + lst[:(i + c) % n]

def run(inp, moves):
    cups = [int(x) for x in inp]

    print('p1: {}'.format(p1(cups.copy(), moves)))
    print('p2: {}'.format(p2(cups.copy(), 10, len(cups))))
    print('p2: {}'.format(p2(cups.copy(), int(1e7), int(1e6))))

def p2(cups, moves, n):
    cups = Cycle(cups + list(range(len(cups) + 1, n + 1)))
    for rnd in range(moves):
        if rnd % 1000000 == 0:
            print(rnd / moves)
        if n < 1000:
            print(cups)

        curr = cups.cycle()
        pick, pick_cs = cups.remove3()

        if n < 1000:
            print(pick_cs)

        dst = (curr - 1) % (n + 1)
        while dst == 0 or dst in pick_cs:
            dst = (dst - 1) % (n + 1)

        cups.insert_at(dst, pick)

    if n < 100:
        print(cups)

    cups.cycle_until(1)
    cups.cycle()
    return cups.pop() * cups.pop()

def p1(cups, moves):
    n = len(cups)
    curr = cups[0]
    for rnd in range(moves):
        #print('--- move {} ---'.format(rnd + 1))
        #print('cups: {}: {}'.format(cups, curr))

        pick = nslice(cups, cups.index(curr) + 1, 3)
        for p in pick:
            cups.remove(p)

        dst = (curr - 1) % (n + 1)
        while dst == 0 or dst in pick:
            dst = (dst - 1) % (n + 1)

        #print('pick: {}'.format(pick))
        #print('dst: {}'.format(dst))

        dst_i = (cups.index(dst) + 1) % n
        cups = cups[:dst_i] + pick + cups[dst_i:]
        curr = cups[(cups.index(curr) + 1) % n]

    return ''.join([str(c) for c in nslice(cups, cups.index(1) + 1, n - 1)])

if __name__ == '__main__':
    run('389125467', 100)
    run('942387615', 100)
