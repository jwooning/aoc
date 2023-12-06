#!/usr/bin/env python

import itertools
import collections

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  times = []
  records = []

  for l in inp:
    if l.startswith('Time:'):
      times = [int(x) for x in l.split(':')[1].strip().split()]
    elif l.startswith('Distance:'):
      records = [int(x) for x in l.split(':')[1].strip().split()]

  assert len(times) == len(records)
  wins = [0] * len(times)

  for speed in range(max(times)):
    for i, (time, record) in enumerate(zip(times, records)):
      time_left = time - speed
      dist = speed * time_left

      if dist > record:
        wins[i] += 1

  p1 = 1
  for w in wins:
    p1 *= w

  print(f'p1: {p1}')

if __name__ == '__main__':
  solve_input()
