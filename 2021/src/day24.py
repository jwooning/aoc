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

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  lines = [x for x in in_ if x]

  q = collections.deque([(0, 0, [])])
  k = 0
  while len(q):
    i, z, js = q.popleft()
    for j in range(1, 10):
      new_js = js.copy()
      new_js.append(j)
      new_z = step(j, i, z)
      if new_z is None:
        continue

      if i == 12:
        if new_z <= 9:
          # assert do(lines, new_js) == new_z
          print('!!!', new_js + [new_z])
          return
      else:
        q.appendleft((i+1, new_z, new_js))
    k += 1
    if k % 100000 == 0:
      print(k, len(q), i, j, js)


def step(in_, i, z):
  l2 = [-1, -1, -1, 11, -1, -1, -1,  7, -1, 6, 10, 15,  9, 0]
  l3 = [ 6, 12,  8,  7,  7, 12,  2, 15,  4, 5, 12, 11, 13, 7]

  if l2[i] >= 0:
    x = z % 26
    z //= 26

    if x != in_ + l2[i]:
      return None
      z *= 26
      z += in_
      z += l3[i]

  else:
    z *= 26
    z += in_
    z += l3[i]

  return z

def do(lines, inputs):
  var = collections.defaultdict(lambda: 0)
  inputs_i = 0
  for l in lines:
    if l.startswith('inp'):
      _, v = l.split()
      var[v] = inputs[inputs_i]
      inputs_i += 1
    elif l.startswith('add'):
      _, v1, v2_ = l.split()
      try:
        v2 = int(v2_)
      except ValueError:
        v2 = var[v2_]
      var[v1] += v2
    elif l.startswith('mul'):
      _, v1, v2_ = l.split()
      try:
        v2 = int(v2_)
      except ValueError:
        v2 = var[v2_]
      var[v1] *= v2
    elif l.startswith('div'):
      _, v1, v2_ = l.split()
      try:
        v2 = int(v2_)
      except ValueError:
        v2 = var[v2_]
      var[v1] //= v2
    elif l.startswith('mod'):
      _, v1, v2_ = l.split()
      try:
        v2 = int(v2_)
      except ValueError:
        v2 = var[v2_]
      var[v1] %= v2
    elif l.startswith('eql'):
      _, v1, v2_ = l.split()
      try:
        v2 = int(v2_)
      except ValueError:
        v2 = var[v2_]
      var[v1] = int(var[v1] == v2)

  return var['z']

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_)
