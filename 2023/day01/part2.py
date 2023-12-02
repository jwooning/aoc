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

for x in range(1, 10):
  strs[str(x)] = str(x)

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  p2 = 0
  for l in inp:
    lidx = int(1e6)
    lvals = {}
    ridx = -1
    rvals = {}
    for k, v in strs.items():
      if k in l:
        idx = l.index(k)
        lidx = min(lidx, idx)
        lvals[idx] = v

        idx = l.rindex(k)
        ridx = max(ridx, idx)
        rvals[idx] = v

    p2 += int(lvals[lidx] + rvals[ridx])

  print(f'p2: {p2}')

if __name__ == '__main__':
  solve(['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen'])
  solve_input()
