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
  p1 = 0
  for l in inp:
    l = [ch for ch in l]
    c1 = set(l[:len(l)//2])
    c2 = set(l[len(l)//2:])
    both = c1 & c2
    assert len(both) == 1
    p1 += priority(next(iter(both)))

  print(f'p1: {p1}')

if __name__ == '__main__':
  solve_input()
