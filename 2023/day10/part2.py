#!/usr/bin/env python

import copy
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

LEFT = {
  N: W,
  E: N,
  S: E,
  W: S,
}

RIGHT = {
  N: E,
  E: S,
  S: W,
  W: N,
}

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  grid = []
  start = None
  dots = 0
  for y, l in enumerate(inp):
    grid.append([c for c in l])
    for c in l:
      if c == '.':
        dots += 1

    if 'S' in grid[-1]:
      start = (y, grid[-1].index('S'))

  print(f'dots: {dots}')
  loop_part = find_loop_part(grid, start)
  for y in range(len(grid)):
    for x in range(len(grid[0])):
      if grid[y][x] != '.' and (y, x) not in loop_part:
        grid[y][x] = '*'

  p2l = inner(copy.deepcopy(grid), start, LEFT)
  p2r = inner(copy.deepcopy(grid), start, RIGHT)
  print(f'p2l: {p2l}')
  print(f'p2r: {p2r}')

def find_loop_part(grid, start):
  res = set([start])
  prev = start
  y = prev[0] + N[0]
  x = prev[1] + N[1]

  while (y, x) != start:
    tile = grid[y][x]

    s0, s1 = DIRS[tile]
    step = s1 if (y + s0[0], x + s0[1]) == prev else s0

    res.add((y, x))

    prev = (y, x)
    y += step[0]
    x += step[1]

  return res

def inner(grid, start, INNER):
  prev = start
  y = start[0] + N[0]
  x = start[1] + N[1]
  res = 0
  p1 = 1

  while (y, x) != start:
    tile = grid[y][x]

    s0, s1 = DIRS[tile]
    step = s1 if (y + s0[0], x + s0[1]) == prev else s0
    left = INNER[step]

    q = collections.deque([(y + left[0], x + left[1])])
    while len(q):
      ly, lx = q.popleft()
      if 0 <= ly < len(grid) and 0 <= lx < len(grid[0]) and grid[ly][lx] in ('.', '*'):
        if grid[ly][lx] == '.':
          res += 1

        grid[ly][lx] = '%'
        for dir_ in (N, E, S, W):
          q.appendleft((ly + dir_[0], lx + dir_[1]))

    prev = (y, x)
    y += step[0]
    x += step[1]
    p1 += 1

  p1 /= 2

  print(f'p1: {p1}')

  return res

if __name__ == '__main__':
  solve_input()
