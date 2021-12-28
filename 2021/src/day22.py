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

  coordss = []
  splits = [[], [], []]
  for l in lines:
    res = int(l[1] == 'n')
    input_ = [x.split('=')[1] for x in l.split(' ')[1].split(',')]
    coords = []
    for i, in_ in enumerate(input_):
      _0, _1 = [int(x) for x in in_.split('..')]
      coords.append([_0, _1 + 1])
      splits[i] += [_0, _1 + 1]
    coordss.append((res, coords))

  splits = [sorted(list(set(x))) for x in splits]
  print(len(splits[0]), len(splits[1]), len(splits[2]))

  grid3 = np.zeros((len(splits[0]), len(splits[1]), len(splits[2])), dtype=np.uint8)

  for i, (res, (xs, ys, zs)) in enumerate(coordss):
    xis = [i for i, s in enumerate(splits[0]) if xs[0] <= s < xs[1]]
    yis = [i for i, s in enumerate(splits[1]) if ys[0] <= s < ys[1]]
    zis = [i for i, s in enumerate(splits[2]) if zs[0] <= s < zs[1]]
    for x, y, z in itertools.product(xis, yis, zis):
      grid3[x, y, z] = res

    print(i)
    if i == 19 or i == len(coordss) - 1:
      res = 0
      for x in range(0, len(splits[0])-1):
        xr = splits[0][x + 1] - splits[0][x]
        for y in range(0, len(splits[1])-1):
          yr = splits[1][y + 1] - splits[1][y]
          for z in range(0, len(splits[2])-1):
            zr = splits[2][z + 1] - splits[2][z]
            if grid3[x, y, z]:
              res += xr * yr * zr

      print(f'res: {res}')

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_)
