#!/usr/bin/env python

import itertools

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  p1 = 0
  p2 = 0
  for l in inp:
    e1, e2 = l.split(',')
    e1 = e1.split('-')
    e2 = e2.split('-')
    e1 = set(range(int(e1[0]), int(e1[1])+1))
    e2 = set(range(int(e2[0]), int(e2[1])+1))

    if e1 <= e2 or e2 <= e1:
      p1 += 1

    p2 += int(len(e1 & e2) > 0)

  print(f'p1: {p1}')
  print(f'p2: {p2}')

if __name__ == '__main__':
  solve_input()
