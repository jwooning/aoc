#!/usr/bin/env python

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def is_correct(l1, l2):
  if isinstance(l1, int) and isinstance(l2, int):
    if l1 == l2:
      return None
    return l1 < l2
  elif isinstance(l1, list) and isinstance(l2, list):
    for v1, v2 in zip(l1, l2):
      r1 = is_correct(v1, v2)
      if r1 is not None:
        return r1
    if len(l1) == len(l2):
      return None
    return len(l1) < len(l2)
  elif isinstance(l1, list):
    return is_correct(l1, [l2])
  elif isinstance(l2, list):
    return is_correct([l1], l2)

class Packet:
  def __init__(self, v):
    self.val = v

  def __lt__(self, o):
    return is_correct(self.val, o.val)

  def __str__(self):
    return f'Packet({self.val})'

def solve(inp):
  ps = [
    Packet([[2]]),
    Packet([[6]]),
  ]
  for l in inp:
    if len(l):
      vl = eval(l)
      ps.append(Packet(vl))

  ps = sorted(ps)

  p2 = 1
  for i, p in enumerate(ps, start=1):
    if p.val in ([[2]], [[6]]):
      p2 *= i
  print(f'p2: {p2}')

if __name__ == '__main__':
  # solve(['[1,1,3,1,1]', '[1,1,5,1,1]', '', '[[1],[2,3,4]]', '[[1],4]', '', '[9]', '[[8,7,6]]', '', '[[4,4],4,4]', '[[4,4],4,4,4]', '', '[7,7,7,7]', '[7,7,7]', '', '[]', '[3]', '', '[[[]]]', '[[]]', '', '[1,[2,[3,[4,[5,6,7]]]],8,9]', '[1,[2,[3,[4,[5,6,0]]]],8,9]'])
  solve_input()
