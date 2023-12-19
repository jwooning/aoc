#!/usr/bin/env python

import itertools
import collections
import functools

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def extrapolate(nums):
  all_zero = True
  for x in nums:
    if x != 0:
      all_zero = False
      break

  if all_zero:
    return 0

  diffs = []
  prev = nums[0]
  for x in nums[1:]:
    diffs.append(x - prev)
    prev = x

  return nums[0] - extrapolate(diffs)

def solve(inp):
  p2 = 0

  for l in inp:
    nums = [int(x) for x in l.split()]

    p2 += extrapolate(nums)

  print(f'p2: {p2}')

if __name__ == '__main__':
  solve_input()
