#!/usr/bin/env python

import itertools
import collections

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  name = None
  vals = None
  dst_name = None
  dst_vals = set()

  for l in inp:
    print(l)
    if l.startswith('seeds:'):
      name = 'seed'
      vals = set([int(x) for x in l.split()[1:]])

    elif l.endswith('map:'):
      src_name, dst_name = l.split()[0].split('-to-')
      assert src_name == name

    elif len(l):
      dst_range, src_range, range_len = [int(x) for x in l.split()]

      for v in list(vals):
        if src_range <= v < src_range + range_len:

          vals.remove(v)
          dst_vals.add(dst_range + (v - src_range))

    elif dst_name is not None:
      name = dst_name
      vals |= dst_vals
      dst_name = None
      dst_vals = set()

  name = dst_name
  vals |= dst_vals
  dst_name = None
  dst_vals = set()

  assert name == 'location'

  p1 = sorted(list(vals))[0]

  print(f'p1: {p1}')

if __name__ == '__main__':
  solve_input()
