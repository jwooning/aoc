#!/usr/bin/env python

import itertools
import collections
import functools

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  p1 = 0

  l0 = inp[0]
  idxs = {'L': 0, 'R': 1}

  routes = {}
  for l in inp[2:]:
    src, dsts = l.split(' = ')
    dst0, dst1 = dsts[1:-1].split(', ')
    routes[src] = (dst0, dst1)

  dst = 'ZZZ'
  f = 'AAA'
  while f != dst:
    idx = idxs[l0[p1 % len(l0)]]
    f = routes[f][idx]
    p1 += 1

  print(f'p1: {p1}')

if __name__ == '__main__':
  solve_input()
