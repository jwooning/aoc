#!/usr/bin/env python
import os
import sys
import struct
import copy
import itertools
import collections

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  lines = [x for x in in_ if x]

  grid1 = []
  for l in lines:
    grid1.append([int(x) for x in l])
  calc(grid1)

  grid2 = []
  for i in range(5):
    for l in lines:
      line = []
      for j in range(5):
        for c in l:
          x = int(c) + i + j
          while x > 9:
            x -= 9
          line.append(x)

      grid2.append(line)
  calc(grid2)

def calc(grid):
  scores = {(0, 0): 0}
  todo = collections.deque([(0, 0)])
  while len(todo):
    x, y = todo.popleft()
    if x > 0 and ((x - 1, y) not in scores or scores[(x, y)] + grid[y][x - 1] < scores[(x - 1, y)]):
      scores[(x - 1, y)] = scores[(x, y)] + grid[y][x - 1]
      todo.append((x - 1, y))
    if x < len(grid[0]) - 1 and ((x + 1, y) not in scores or scores[(x, y)] + grid[y][x + 1] < scores[(x + 1, y)]):
      scores[(x + 1, y)] = scores[(x, y)] + grid[y][x + 1]
      todo.append((x + 1, y))
    if y > 0 and ((x, y - 1) not in scores or scores[(x, y)] + grid[y - 1][x] < scores[(x, y - 1)]):
      scores[(x, y - 1)] = scores[(x, y)] + grid[y - 1][x]
      todo.append((x, y - 1))
    if y < len(grid) - 1 and ((x, y + 1) not in scores or scores[(x, y)] + grid[y + 1][x] < scores[(x, y + 1)]):
      scores[(x, y + 1)] = scores[(x, y)] + grid[y + 1][x]
      todo.append((x, y + 1))

  print(scores[(len(grid[0]) - 1, len(grid) - 1)])

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_)
