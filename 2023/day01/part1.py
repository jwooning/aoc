#!/usr/bin/env python

import itertools

strs = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9',
}

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  p1 = 0
  p2 = 0
  for l in inp:
    digits = [x for x in l if x.isdigit()]
    p1 += int(digits[0] + digits[-1])

    l2 = l
    for k, v in strs.items():
      l2.replace(k, v)

    digits = [x for x in l if x.isdigit()]
    p2 += int(digits[0] + digits[-1])

  print(f'p1: {p1}')
  print(f'p2: {p2}')

if __name__ == '__main__':
  solve(['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet'])
  solve_input()
