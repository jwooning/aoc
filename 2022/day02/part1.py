#!/usr/bin/env python

import itertools

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  points = {
    'X': 1,
    'Y': 2,
    'Z': 3,
  }
  win = {
    'A': {
      'X': 3, 'Y': 6, 'Z': 0,
    },
    'B': {
      'X': 0, 'Y': 3, 'Z': 6,
    },
    'C': {
      'X': 6, 'Y': 0, 'Z': 3,
    },
  }

  p1 = 0
  p2 = 0
  for l in inp:
    o, s = l.split()
    p1 += points[s]
    p1 += win[o][s]

    if s == 'X':
      p2 += 0
      p2 += points[[k for k, v in win[o].items() if v == 0][0]]
    elif s == 'Y':
      p2 += 3
      p2 += points[[k for k, v in win[o].items() if v == 3][0]]
    elif s == 'Z':
      p2 += 6
      p2 += points[[k for k, v in win[o].items() if v == 6][0]]

  print(f'p1: {p1}')
  print(f'p2: {p2}')

if __name__ == '__main__':
  solve_input()
