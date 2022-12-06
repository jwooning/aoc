#!/usr/bin/env python

import itertools

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    solve(file_content)

def solve(inp):
  stacks = []
  for _ in range(9):
    stacks.append([])

  for i in range(7, -1, -1):
    for j in range(0, 9):
      jdx = j*4 + 1
      if inp[i][jdx].isupper():
        stacks[j].append(inp[i][jdx])

  for l in inp[10:]:
    lspl = l.split(' ')
    c, f, t = lspl[1], lspl[3], lspl[5]
    c, f, t = int(c), int(f), int(t)

    for _ in range(c):
      stacks[t-1].append(stacks[f-1].pop())

  p1 = ''.join([x[-1] for x in stacks])
  print(f'p1: {p1}')

if __name__ == '__main__':
  solve_input()
