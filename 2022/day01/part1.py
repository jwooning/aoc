#!/usr/bin/env python

import itertools

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  elves = []
  curr = 0
  for l in inp:
    if l:
      curr += int(l)
    else:
      elves.append(curr)
      curr = 0

  elves = sorted(elves, reverse=True)
  p1 = elves[0]
  print(f'p1: {p1}')

  p2 = sum(elves[:3])
  print(f'p2: {p2}')

if __name__ == '__main__':
  solve_input()
