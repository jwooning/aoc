#!/usr/bin/env python
import os
import sys
import struct

from functools import lru_cache


def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  lines = list(in_)
  crabs = [int(x) for x in lines[0].split(',')]
  p1 = 1000000000000000000000000
  p2 = 1000000000000000000000000
  costs = [0] * (max(crabs) + 1)
  for i in range(1, max(crabs) + 1):
    costs[i] = costs[i - 1] + i
  for i in range(min(crabs), max(crabs) + 1):
    cost1 = sum([abs(c - i) for c in crabs])
    p1 = min(cost1, p1)
    cost2 = sum([costs[abs(c - i)] for c in crabs])
    p2 = min(cost2, p2)

  print(f'p1 {p1}')
  print(f'p2 {p2}')


if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_)
