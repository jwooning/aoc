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
  folds = []
  dots = set()
  for l in lines:
    if l.startswith('fold'):
      dir_, at = l.split('fold along ')[1].split('=')
      folds.append((dir_, int(at)))
    else:
      dots.add(tuple([int(x) for x in l.split(',')]))

  for i, (dir_, at) in enumerate(folds):
    new_dots = set()
    for x, y in list(dots):
      if dir_ == 'y':
        if y > at:
          new_dots.add((x, at - (y - at)))
        elif y < at:
          new_dots.add((x, y))

      else:
        if x > at:
          new_dots.add((at - (x - at), y))
        elif x < at:
          new_dots.add((x, y))

    if i == 0:
      print(f'p1: {len(list(new_dots))}')

    dots = new_dots.copy()

  max_x = max([x for x, y in list(dots)])
  max_y = max([y for x, y in list(dots)])
  grid = [[' '] * (max_x+1) for _ in range(max_y+1)]
  for x, y in list(dots):
    grid[y][x] = '#'

  for l in grid:
    print(l)

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_)
