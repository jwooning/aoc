#!/usr/bin/env python

import itertools

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def rotate(prev, op):
  if op[0] == 'L':
    return (prev - int(op[1:])) % 100
  elif op[0] == 'R':
    return (prev + int(op[1:])) % 100

def solve(inp):
  f = 50
  p1 = 0
  for l in inp:
    f = rotate(f, l)

    if f == 0:
      p1 += 1

  print(f'p1: {p1}')

if __name__ == '__main__':
  solve(['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82'])
  solve_input()
