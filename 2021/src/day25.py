#!/usr/bin/env python
import os
import sys
import struct
import copy
import math
import time
import itertools
import collections
import uuid

import numpy as np

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  lines = [x for x in in_ if x]
  h = len(lines)
  w = len(lines[0])

  grid = np.zeros((h, w), dtype=np.uint8)
  for y, l in enumerate(lines):
    for x, ch in enumerate(l):
      if ch == '>':
        grid[y, x] = 1
      elif ch == 'v':
        grid[y, x] = 2

  print(grid)

  i = 0
  ngrid = np.zeros((h, w), dtype=np.uint8)
  while True:
    ngrid.fill(0)

    for y, x in zip(*np.nonzero(grid == 1)):
      nx = (x + 1) % w
      if grid[y, nx] == 0:
        ngrid[y, nx] = 1
      else:
        ngrid[y, x] = 1

    for y, x in zip(*np.nonzero(grid == 2)):
      ny = (y + 1) % h
      if grid[ny, x] != 2 and ngrid[ny, x] != 1:
        ngrid[ny, x] = 2
      else:
        ngrid[y, x] = 2

    i += 1
    if np.array_equal(grid, ngrid):
      print('!!!')
      print(grid)
      print(i)
      return

    grid = np.copy(ngrid)
    #print(grid)
    #print(i)
    #time.sleep(1)

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  #input_ = ['v...>>.vv>', '.vv>>.vv..', '>>.>v>...v', '>>v>>.>.v.', 'v>v.vv.v..', '>.>>..v...', '.vv..>.>v.', 'v.v..>>v.v', '....v..v.>']
  run(input_)
