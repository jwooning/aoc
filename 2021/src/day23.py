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

dest = {
  1: 2,
  10: 4,
  100: 6,
  1000: 8,
}

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def path(sp, from_, to):
  if from_[1] > to[1]:
    from_, to = to, from_

  for pos, ant in sp.items():
    if ant is not None and pos[0] == 0 and pos != from_ and pos != to and from_[1] <= pos[1] <= to[1]:
      return False

  return True

def run(in_):
  lines = [x for x in in_ if x]
  lines = lines[:3] + ['  #D#C#B#A#', '  #D#B#A#C#'] + lines[3:]
  spaces = {}
  depth = len(lines) - 2
  for i, l in enumerate(lines[1:depth+1]):
    for j, ch in enumerate(l[1:][:-1]):
      if ch in ['#', ' ']:
        continue
      if (0, j) in spaces:
        del spaces[(0, j)]
      spaces[(i, j)] = None if ch == '.' else (10 ** (ord(ch) - 65))

  print(spaces)

  q = collections.deque([(0, spaces.copy())])
  p1 = int(10e10)
  while len(q):
    cost, sp = q.popleft()
    if cost > p1:
      continue

    # done?
    done = True
    for pos, ant in sp.items():
      if ant is not None and pos[1] != dest[ant]:
        done = False

    if done:
      p1 = min(p1, cost)
      print(p1)

    # any amphipod that can move in position
    work = False
    for pos, ant in sp.items():
      if pos[0] == 0 and ant is not None:
        d = dest[ant]
        valid = True
        c = 1
        for i in range(1, depth):
          if sp[(i, d)] != ant and sp[(i, d)] is not None:
            valid = False
            break

          if sp[(i, d)] is None:
            c = i

        if valid and path(sp, pos, (i, d)):
          new_sp = sp.copy()
          new_sp[pos] = None
          new_sp[(c, d)] = ant
          new_cost = cost + ((abs(c - pos[0]) + abs(d - pos[1])) * ant)
          q.appendleft((new_cost, new_sp))
          work = True
          break

    if work:
      continue

    # try random
    for d in dest.values():
      c = None
      for i in range(1, depth):
        if sp[(i, d)] is not None:
          c = i
          break
      if c is None:
        continue

      ant = sp[(c, d)]
      if dest[ant] == d:
        all_ = True
        for i in range(c + 1, depth):
          if sp[(i, d)] != ant:
            all_ = False
            break
        if all_:
          continue

      for pos, dant in sp.items():
        if pos[0] == 0 and dant is None and path(sp, (c, d), pos):
          new_sp = sp.copy()
          new_sp[(c, d)] = None
          new_sp[pos] = ant
          new_cost = cost + ((abs(c - pos[0]) + abs(d - pos[1])) * ant)
          q.appendleft((new_cost, new_sp))

  print(f'p1: {p1}')


if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  #input_ = ['#############', '#...........#', '###B#C#B#D###', '  #A#D#C#A#', '  #########']
  run(input_)
