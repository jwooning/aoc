#!/usr/bin/env python
import os
import sys
import struct
import copy
import math
import time
import itertools
import collections

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  lines = [x for x in in_ if x]
  algo = None
  img = []
  for l in lines:
    l = ['1' if ch == '#' else '0' for ch in l]
    if algo is None:
      algo = l
    else:
      img.append(l)

  edge = '0'
  for _ in range(50):
    img, edge = step(algo, img, edge)

  p1 = 0
  for l in img:
    p1 += sum([int(ch) for ch in l])
  print(f'p1: {p1}')

def step(algo, img, edge):
  img = [([edge] * 2) + l + ([edge] * 2) for l in img]
  empty = [edge] * len(img[0])
  img = ([empty] * 2) + img + ([empty] * 2)

  res = []
  for y in range(1, len(img) - 1):
    res.append([])
    for x in range(1, len(img[0]) - 1):
      bin_ = ''.join(img[y-1][x-1:x+2] + img[y][x-1:x+2] + img[y+1][x-1:x+2])
      res[-1].append(algo[int(bin_, 2)])

  edge = algo[int(''.join([edge] * 9), 2)]

  return res, edge

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_)
