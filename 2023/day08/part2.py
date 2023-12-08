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
  l0 = inp[0]
  idxs = {'L': 0, 'R': 1}

  fs = []
  ds = []
  routes = {}
  for l in inp[2:]:
    src, dsts = l.split(' = ')
    dst0, dst1 = dsts[1:-1].split(', ')
    routes[src] = (dst0, dst1)

    for l in [src, dst0, dst1]:
      if l[-1] == 'A' and l not in fs:
        fs.append(l)
      if l[-1] == 'Z' and l not in ds:
        ds.append(l)

  assert len(fs) == len(ds)
  n = len(fs)

  solv = []
  for _ in range(n):
    solv.append({})

  # TODO somehow iterate indivually and find combined pattern in l0 and locations
  for i in range(n):
    steps = 0
    while len(solv[i]) < n:
      dirn = steps % len(l0)
      key = (dirn, fs[i])
      if fs[i].endswith('Z'):
        solv[i][key] = steps

      if key in solv[i]:  # circular
        break

      idx = idxs[l0[dirn]]
      fs[i] = routes[fs[i]][idx]

      steps += 1

    print('fin')
  print(f'p2: {p2}')

if __name__ == '__main__':
  solve_input()
