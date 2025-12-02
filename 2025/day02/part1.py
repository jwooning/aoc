#!/usr/bin/env python

import itertools

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  p1 = 0
  numbers = []
  for l in inp:
    for r in l.split(','):
      ids = [int(x) for x in r.split('-')]
      numbers += list(range(ids[0], ids[1] + 1))

  for num in numbers:
    strnum = str(num)

    i = len(strnum) // 2
    if len(strnum) == 1 or len(strnum) / 2 != i:
      continue

    is_valid = False
    for j in range(i, len(strnum), i):
      if strnum[:i] != strnum[j: j+i]:
        is_valid = True
        break

    if not is_valid:
      p1 += num

  print(f'p1: {p1}')

if __name__ == '__main__':
  solve(['11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'])
  solve_input()
