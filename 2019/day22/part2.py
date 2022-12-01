#!/usr/bin/env python

import math
from collections import defaultdict

def solve_input(file):
  with open(file, 'r') as f:
    file_content = f.read()
    solve(file_content)

def new_stack(cards):
  return cards[::-1]

def cut(cards, n):
  return cards[n:] + cards[:n]

def increment(cards, n):
  res = [-1] * len(cards)
  i = 0
  for c in cards:
    res[i] = c
    i = (i + n) % len(cards)

  return res

class Slice:
  def __init__(self, start, stop, step):
    self.start = start
    self.stop = stop
    self.step = step

  def __eq__(self, o):
    return self.start == o.start and self.stop == o.stop and self.step == o.step

  def __hash__(self):
    return hash([self.start, self.stop, self.step])

def solve(inp):
  cards = {}
  cards[Slice(0, 119315717514047, 1)] = Slice(0, 119315717514047, 1)

  for _ in range(101741582076661):
    for line in inp.split('\n'):
      if line.startswith('deal into new stack'):
        cards = new_stack(cards)
      elif line.startswith('cut'):
        n = int(line.split(' ')[-1])
        cards = cut(cards, n)
      elif line.startswith('deal with increment'):
        n = int(line.split(' ')[-1])
        cards = increment(cards, n)

  p2 = cards[2020]

  print(f'p1: {p2}')

if __name__ == '__main__':
  solve_input('input')
