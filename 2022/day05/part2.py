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

    stacks[t-1] += stacks[f-1][-c:]
    stacks[f-1] = stacks[f-1][:-c]

  p2 = ''.join([x[-1] for x in stacks])
  print(f'p2: {p2}')

if __name__ == '__main__':
  solve_input()
