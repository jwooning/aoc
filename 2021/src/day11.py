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

def print_o(octo):
  for o in octo:
    print(o)

def step(octo):
  flashed = set()
  for x, y in itertools.product(range(10), range(10)):
    octo[x][y] += 1
    if octo[x][y] > 9:
      flash(octo, flashed, x, y)

  res = len(flashed)
  for x, y in list(flashed):
    octo[x][y] = 0

  return res

def flash(octo, flashed, x, y):
  if (x, y) in flashed:
    return

  flashed.add((x, y))

  for i, j in itertools.product(range(-1, 2), range(-1, 2)):
    if i == 0 and j == 0:
      continue

    if 0 <= x+i < 10 and 0 <= y+j < 10:
      octo[x+i][y+j] += 1
      if octo[x+i][y+j] > 9:
        flash(octo, flashed, x+i, y+j)

def run(in_):
  lines = [x for x in in_ if x]
  octo = [[0] * 10 for _ in range(10)]

  for x, l in enumerate(lines):
    for y, ch in enumerate(l):
      octo[x][y] = int(ch)

  p1 = 0
  p2 = 0
  i = 0
  while True:
    i += 1

    st = step(octo)
    if i <= 100:
      p1 += st

    if st == 100:
      p2 = i
      break

  print(f'p1: {p1}')
  print(f'p2: {p2}')

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_)
