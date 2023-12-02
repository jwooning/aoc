#!/usr/bin/env python

import itertools

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

limits = {
  'red': 12,
  'green': 13,
  'blue': 14,
}

def solve(inp):
  p1 = 0
  for l in inp:
    gid, gl = l.split(':')
    gid = int(gid.split()[-1])

    valid = True

    for game in gl.split(';'):
      for c in game.split(','):
        val, color = c.split()
        if int(val) > limits[color]:
          valid = False

    if valid:
      p1 += gid

  print(f'p1: {p1}')

if __name__ == '__main__':
  solve_input()
