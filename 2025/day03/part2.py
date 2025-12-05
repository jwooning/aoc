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
  batteries = 12
  p2 = 0
  for l in inp:
    ress = []
    j = 0
    for i in range(batteries):
      if -batteries+i+1 != 0:
        new_j, res = highest(l[j: -batteries+i+1])
      else:
        new_j, res = highest(l[j:])

      j = j + new_j + 1
      ress.append(res)

    jolts = int(''.join([str(x) for x in ress]))

    p2 += jolts

  print(f'p2: {p2}')

if __name__ == '__main__':
  solve(['987654321111111', '811111111111119', '234234234234278', '818181911112111'])
  solve_input()
