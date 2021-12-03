#!/usr/bin/env python
import os
import sys
import struct

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def bit_count(lines):
  bc = None
  for l in lines:
    if not bc:
      n = len(l)
      bc = [[0, 0] for _ in range(len(l))]

    for i, ch in enumerate(l):
      bc[i][int(ch)] += 1

  bc0 = [1 if _0 > _1 else 0 for _0, _1 in bc]
  bc1 = [1 if _1 >= _0 else 0 for _0, _1 in bc]

  return bc0, bc1

def bits_to_int(l):
  n = len(l)
  res = 0
  for i, ch in enumerate(l):
    if int(ch):
      res += 1 << (n - i - 1)
  return res

def run(in_):
  lines = [x for x in in_ if x]
  n = len(lines[0])
  bc0, bc1 = bit_count(lines)

  print(bc0)
  print(bc1)

  gamma = 0
  epsilon = 0

  for i, cn in enumerate(bc0):
    if cn:
      gamma += 1 << (n - i - 1)
    else:
      epsilon += 1 << (n - i - 1)

  print(f'p1: {gamma} * {epsilon}: {gamma * epsilon}')

  oxy = lines.copy()
  co2 = lines.copy()
  for i in range(n):
    _, bco = bit_count(oxy)
    bcc, _ = bit_count(co2)
    if len(oxy) > 1:
      oxy = [x for x in oxy if int(x[i]) == bco[i]]
    if len(co2) > 1:
      co2 = [x for x in co2 if int(x[i]) == bcc[i]]

    print(i, bco, oxy)
    print(i, bcc, co2)

  print(oxy, bits_to_int(oxy[0]))
  print(co2, bits_to_int(co2[0]))
  print(bits_to_int(oxy[0]) * bits_to_int(co2[0]))

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  #input_ = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
  run(input_)
