#!/usr/bin/env python

import copy
import itertools
import collections

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  p2 = 0
  m = []
  for l in inp:
    m.append([0] + [1 if x == '@' else 0 for x in l] + [0])

  empty = [[0] * (len(l) + 2)]
  m = empty + m + empty

  cont = True
  while cont:
    cont = False
    new_m = copy.deepcopy(m)
    for y in range(1, len(m)):
      for x in range(1, len(l) + 1):
        if not m[y][x]:
          continue

        surroundings = 0
        for dx, dy in itertools.product([-1, 0, 1], repeat=2):
          if dx == 0 and dy == 0:
            continue

          if m[y+dy][x+dx]:
            surroundings += 1

        if surroundings < 4:
          p2 += 1
          cont = True
          new_m[y][x] = 0

    m = copy.deepcopy(new_m)

  print(f'p2: {p2}')

if __name__ == '__main__':
  solve([
    '..@@.@@@@.',
    '@@@.@.@.@@',
    '@@@@@.@.@@',
    '@.@@@@..@.',
    '@@.@@@@.@@',
    '.@@@@@@@.@',
    '.@.@.@.@@@',
    '@.@@@.@@@@',
    '.@@@@@@@@.',
    '@.@.@@@.@.',
  ])
  solve_input()
