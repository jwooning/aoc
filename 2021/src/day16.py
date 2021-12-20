#!/usr/bin/env python
import os
import sys
import math
import struct
import copy
import itertools
import collections

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  line = list(in_)[0]
  bitstring = bin(int(line, 16))[2:]
  bin_ = bitstring.rjust(len(line)*4, '0')
  print(bin_)
  i, p1, p2 = calc(bin_, 0)
  print(f'p1: {p1}')
  print(f'p2: {p2}')

def calc(bin_, i):
  version = int(bin_[i:i+3], 2)
  type_ = int(bin_[i+3:i+6], 2)
  p1 = version

  print(version, type_)

  i += 6
  if type_ == 4:
    res = ''
    while True:
      res += bin_[i+1:i+5]
      if bin_[i] == '0':
        i += 5
        break
      i += 5

    print(int(res, 2))
    return i, p1, int(res, 2)

  else:
    len_type = bin_[i]
    i += 1
    vals = []
    if len_type == '0':
      subs_len = int(bin_[i:i+15], 2)
      i += 15
      old_i = i
      while i < old_i + subs_len:
        i, p1n, p2 = calc(bin_, i)
        p1 += p1n
        vals.append(p2)
    else:
      subs_n = int(bin_[i:i+11], 2)
      i += 11
      for _ in range(subs_n):
        i, p1n, p2 = calc(bin_, i)
        p1 += p1n
        vals.append(p2)

    if type_ == 0:  # sum
      return i, p1, sum(vals)
    elif type_ == 1:  # product
      return i, p1, math.prod(vals)
    elif type_ == 2:  # min
      return i, p1, min(vals)
    elif type_ == 3:  # max
      return i, p1, max(vals)
    elif type_ == 5:  # gt
      return i, p1, int(vals[0] > vals[1])
    elif type_ == 6:  # le
      return i, p1, int(vals[0] < vals[1])
    elif type_ == 7:  # eq
      return i, p1, int(vals[0] == vals[1])

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  #input_ = ['04005AC33890']
  run(input_)
