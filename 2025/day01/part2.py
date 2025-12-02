#!/usr/bin/env python

import itertools

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  f = 50
  p2 = 0
  for l in inp:
    if l[0] == 'L':
      f = (f - int(l[1:]))
    elif l[0] == 'R':
      f = (f + int(l[1:]))

    while f < 0:
      p2 += 1
      f += 100

    while f > 99:
      p2 += 1
      f -= 100

  if f == 0:
    p2 += 1

  print(f'p2: {p2}')

if __name__ == '__main__':
  solve(['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82'])
  solve_input()
