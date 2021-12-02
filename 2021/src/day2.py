#!/usr/bin/env python
import os
import sys

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  x1 = 0
  y1 = 0
  x2 = 0
  y2 = 0
  aim = 0
  for l in in_:
    if not l:
      continue

    dir_, n =l.split(' ')
    n = int(n)
    if dir_ == 'forward':
      x1 += n
      x2 += n
      y2 += n * aim
    elif dir_ == 'down':
      y1 += n
      aim += n
    elif dir_ == 'up':
      y1 -= n
      aim -= n

  print(f'p1: {x1}, {y1}, {x1*y1}')
  print(f'p2: {x2}, {y2}, {x2*y2}')

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_)
