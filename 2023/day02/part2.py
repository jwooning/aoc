#!/usr/bin/env python

import itertools

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  p2 = 0
  for l in inp:
    _, gl = l.split(':')

    mins = {
      'red': 0,
      'green': 0,
      'blue': 0,
    }

    for game in gl.split(';'):
      for c in game.split(','):
        val, color = c.split()
        mins[color] = max(mins[color], int(val))

    pwr = 1
    for v in mins.values():
      pwr *= v

    p2 += pwr

  print(f'p2: {p2}')

if __name__ == '__main__':
  solve_input()
