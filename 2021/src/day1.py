#!/usr/bin/env python
import os
import sys

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  lines = [int(x) for x in in_]
  p1 = 0
  prev = None
  for l in lines:
    if prev:
      if l > prev:
        p1 += 1
    prev = l

  print(f'p1: {p1}')

  p2 = 0
  prev = None
  for i in range(len(lines) - 2):
    new = sum(lines[i: i+3])
    if prev and new > prev:
      p2 += 1
    prev = new

  print(f'p2: {p2}')

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_)
