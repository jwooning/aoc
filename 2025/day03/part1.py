#!/usr/bin/env python

import itertools
import collections

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def highest(l):
  pos = {}
  for i, x in enumerate(l):
    x = int(x)
    if x not in pos:
      pos[x] = i

  for x in range(9, 0, -1):
    if x in pos:
      return pos[x], x

def solve(inp):
  p1 = 0
  for l in inp:

    i, j0 = highest(l[:-1])
    j, j1 = highest(l[i+1:])

    print(i, j0, j, j1)
    p1 += int(str(j0) + str(j1))

  print(f'p1: {p1}')

if __name__ == '__main__':
  solve(['987654321111111', '811111111111119', '234234234234278', '818181911112111'])
  solve_input()
