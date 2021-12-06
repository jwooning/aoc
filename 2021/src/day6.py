#!/usr/bin/env python
import os
import sys
import struct


def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_, days):
  lines = list(in_)
  line = lines[0]
  fish = [0] * 9
  for f in line.split(','):
    fish[int(f)] += 1

  for d in range(days):
    n = fish[0]
    fish = fish[1:] + [n]
    fish[6] += n

  print(f'day {d+1}: {sum(fish)}')

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = ['3,4,3,1,2']
  run(input_, 80)
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_, 80)
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_, 256)
