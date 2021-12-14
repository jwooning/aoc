#!/usr/bin/env python
import os
import sys
import struct
import itertools
from collections import defaultdict

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  lines = [x for x in in_ if x]
  p1 = 0
  low = []
  for i, l in enumerate(lines):
    for j, c in enumerate(l):
      lo = True
      if i > 0 and int(c) >= int(lines[i-1][j]):
        lo = False
      if i < len(lines)-1 and int(c) >= int(lines[i+1][j]):
        lo = False
      if j > 0 and int(c) >= int(lines[i][j-1]):
        lo = False
      if j < len(lines[0])-1 and int(c) >= int(lines[i][j+1]):
        lo = False

      if lo:
        p1 += int(c) + 1
        low.append({(i, j)})

  print(f'p1: {p1}')

  to_calc = list(range(len(low)))
  while len(to_calc):
    new_calc = []
    for i in to_calc:
      new_low = low[i].copy()
      for j, (x, y) in enumerate(low[i]):
        if x > 0 and int(lines[x-1][y]) < 9:
          new_low.add((x-1, y))
        if x < len(lines)-1 and int(lines[x+1][y]) < 9:
          new_low.add((x+1, y))
        if y > 0 and int(lines[x][y-1]) < 9:
          new_low.add((x, y-1))
        if y < len(lines[0])-1 and int(lines[x][y+1]) < 9:
          new_low.add((x, y+1))

      if low[i] != new_low:
        new_calc.append(i)

      low[i].update(new_low)

    to_calc = new_calc.copy()

  sizes = [len(x) for x in low]
  p2 = 1
  for x in sorted(sizes, reverse=True)[:3]:
    p2 *= x
  print(f'p2: {p2}')

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  #input_ = ['2199943210', '3987894921', '9856789892', '8767896789', '9899965678']
  run(input_)
