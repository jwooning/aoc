#!/usr/bin/env python
import os
import sys
import time
import struct
import copy
import itertools
import collections

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  lines = [x for x in in_ if x]
  x, y = [t.split('..') for t in lines[0].split('target area: x=')[1].split(', y=')]
  x = (int(x[0]), int(x[1]))
  y = (int(y[0]), int(y[1]))

  # p1(x, y)
  p2(x, y, 104)
  
def p1(x, y):
  guess = (0, abs(y[1] - y[0]) + 1)
  while True:
    print(guess)
    res, reason = calc(x, y, guess)
    if res:
      print('!!!', guess)
      break
    elif reason == 'x':
      guess = (0, guess[1] - 1)
    elif reason == 'y':
      guess = (guess[0] + 1, guess[1])

  while True:
    res, reason = calc(x, y, guess)
    if res:
      print('!!!', guess, reason)
    guess = (guess[0], guess[1] + 1)

def p2(x, y, y_max):
  p2 = 0
  for i in range(1, x[1] + 1):
    for j in range(y[0], y_max + 1):
      res, reason = calc(x, y, (i, j))
      if res:
        p2 += 1

  print(f'p2: {p2}')
  

def calc(x, y, vel):
  at = (0, 0)
  y_max = 0
  while True:
    at = (at[0] + vel[0], at[1] + vel[1])
    y_max = max(y_max, at[1])
    if at[0] > x[1]:
      return False, 'x'
    if at[1] < y[0]:
      return False, 'y'
    if at[0] >= x[0] and at[1] <= y[1]:
      return True, y_max

    vel = (max(0, vel[0] - 1), vel[1] - 1)

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_)
