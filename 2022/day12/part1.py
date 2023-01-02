#!/usr/bin/env python

import numpy as np
import collections

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  grid = np.empty((len(inp), len(inp[0])), dtype=np.int8)
  for y, l in enumerate(inp):
    for x, ch in enumerate(l):
      if ch == 'S':
        curr = (y, x)
        ch = 'a'
      elif ch == 'E':
        dest = (y, x)
        ch = 'z'

      grid[y, x] = ord(ch) - ord('a')

  q = collections.deque([(curr[0], curr[1], 0)])
  vstd = set((curr[0], curr[1]))
  while len(q):
    y, x, s = q.popleft()
    if (y, x) == dest:
      print(f'p1: {s}')
      break

    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      ny = y + dy
      nx = x + dx
      if 0 <= ny < grid.shape[0] and 0 <= nx < grid.shape[1] \
          and grid[ny, nx] - grid[y, x] <= 1 \
          and (ny, nx) not in vstd:
        vstd.add((ny, nx))
        q.append((ny, nx, s+1))

if __name__ == '__main__':
  # solve(['Sabqponm', 'abcryxxl', 'accszExk', 'acctuvwj', 'abdefghi'])
  solve_input()
