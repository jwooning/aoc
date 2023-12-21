#!/usr/bin/env python

import itertools
import collections
import functools

N = (-1, 0)
E = (0, 1)
S = (1, 0)
W = (0, -1)

DIRS = {
  '|': (N, S),
  '-': (E, W),
  'L': (N, E),
  'J': (N, W),
  '7': (S, W),
  'F': (S, E),
}

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  grid = []
  start = None
  for y, l in enumerate(inp):
    grid.append([c for c in l])
    if 'S' in grid[-1]:
      start = (y, grid[-1].index('S'))

  prev = start
  y = start[0] + N[0]
  x = start[1] + N[1]
  p1 = 1

  while (y, x) != start:
    tile = grid[y][x]

    s0, s1 = DIRS[tile]
    if (y + s0[0], x + s0[1]) == prev:
      prev = (y, x)
      y += s1[0]
      x += s1[1]
    else:
      prev = (y, x)
      y += s0[0]
      x += s0[1]

    p1 += 1

  p1 /= 2
  print(f'p1: {p1}')

if __name__ == '__main__':
  solve_input()
