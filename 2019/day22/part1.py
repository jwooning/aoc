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

def solve(inp, amount=10007):
  cards = list(range(amount))
  print(cards)
  for line in inp.split('\n'):
    if line.startswith('deal into new stack'):
      cards = new_stack(cards)
    elif line.startswith('cut'):
      n = int(line.split(' ')[-1])
      cards = cut(cards, n)
    elif line.startswith('deal with increment'):
      n = int(line.split(' ')[-1])
      cards = increment(cards, n)

    print(cards)

  p1 = [i for i, x in enumerate(cards) if x == 2019]

  print(f'p1: {p1}')

if __name__ == '__main__':
  # solve_input('input')
  solve("deal with increment 2\ndeal with increment 3", 11)
  solve("deal with increment 6", 11)
