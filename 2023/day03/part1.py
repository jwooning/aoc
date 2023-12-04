#!/usr/bin/env python

import itertools

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  p1 = 0
  p2 = 0
  locs = {}

  is_num = False
  curr_start = None
  curr_num = []
  curr_locs = []
  for y, l in enumerate(inp):
    for x, ch in enumerate(l):
      if ch.isdigit():
        if not is_num:
          is_num = True
          curr_start = (x, y)
        curr_num.append(ch)
        curr_locs.append((x, y))

      if is_num and (not ch.isdigit() or x == len(l) - 1):
        num = int(''.join(curr_num))
        locs.update({loc: (curr_start, num) for loc in curr_locs})

        is_num = False
        curr_start = None
        curr_num = []
        curr_locs = []

  for y, l in enumerate(inp):
    for x, ch in enumerate(l):
      if not ch.isdigit() and ch not in ('.', "\n"):
        counted = []
        for dx, dy in itertools.product((-1, 0, 1), repeat=2):
          loc = (x+dx, y+dy)
          if loc in locs:
            start, num = locs[loc]
            if start not in counted:
              p1 += num
              counted.append(start)

      if ch == '*':
        counted = []
        ratios = []
        for dx, dy in itertools.product((-1, 0, 1), repeat=2):
          loc = (x+dx, y+dy)
          if loc in locs:
            start, num = locs[loc]
            if start not in counted:
              ratios.append(num)
              counted.append(start)

        if len(ratios) == 2:
          p2 += ratios[0] * ratios[1]

  print(f'p1: {p1}')
  print(f'p2: {p2}')

if __name__ == '__main__':
  # solve(['467..114..', '...*......', '..35..633.', '......#...', '617*......', '.....+.58.', '..592.....', '......755.', '...$.*....', '.664.598..'])
  # solve(['467..114..', '...*......', '..35..633.', '......#...', '617*......', '.....+.58.', '..592.....', '......755.', '...$.*....', '.664.598..'])
  solve_input()
