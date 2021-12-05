#!/usr/bin/env python
import os
import sys
import struct

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def step(_1, _2):
  if _2 > _1:
    return 1
  if _1 > _2:
    return -1
  return 0

def run(in_):
  lines = [x for x in in_ if x]
  maxs = [0, 0]
  for line in lines:
    (x1, y1), (x2, y2) = [[int(y) for y in x.split(',')] for x in line.split(' -> ')]
    maxs[0] = max(maxs[0], x1 + 1, x2 + 1)
    maxs[1] = max(maxs[1], y1 + 1, y2 + 1)

  grid1 = [[0] * maxs[0] for _ in range(maxs[1])]
  grid2 = [[0] * maxs[0] for _ in range(maxs[1])]
  for line in lines:
    (x1, y1), (x2, y2) = [[int(y) for y in x.split(',')] for x in line.split(' -> ')]
    if x1 == x2:
      s = step(y1, y2)
      for y in range(y1, y2 + s, s):
        grid1[y][x1] += 1
        grid2[y][x1] += 1
    elif y1 == y2:
      s = step(x1, x2)
      for x in range(x1, x2 + s, s):
        grid1[y1][x] += 1
        grid2[y1][x] += 1
    else:
      xs = step(x1, x2)
      ys = step(y1, y2)
      for x, y in zip(range(x1, x2 + xs, xs), range(y1, y2 + ys, ys)):
        grid2[y][x] += 1

  p1 = 0
  for r in grid1:
    for c in r:
      if c > 1:
        p1 += 1

  p2 = 0
  for r in grid2:
    print(r)
    for c in r:
      if c > 1:
        p2 += 1

  print(f'p1: {p1}')
  print(f'p2: {p2}')

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  #input_ = ['0,9 -> 5,9', '8,0 -> 0,8', '9,4 -> 3,4', '2,2 -> 2,1', '7,0 -> 7,4', '6,4 -> 2,0', '0,9 -> 2,9', '3,4 -> 1,4', '0,0 -> 8,8', '5,5 -> 8,2']
  run(input_)
