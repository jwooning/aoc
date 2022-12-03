#!/usr/bin/env python

import itertools

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def priority(letter):
  if letter.isupper():
    return ord(letter) - 38
  else:
    return ord(letter) - 96

def solve(inp):
  p2 = 0
  for i in range(0, len(inp), 3):
    c1 = set([ch for ch in inp[i+0]])
    c2 = set([ch for ch in inp[i+1]])
    c3 = set([ch for ch in inp[i+2]])

    both = c1 & c2 & c3
    assert len(both) == 1
    p2 += priority(next(iter(both)))

  print(f'p2: {p2}')

if __name__ == '__main__':
  solve_input()
