#!/usr/bin/env python

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

DIRS = {
  'R': (1, 0),
  'L': (-1, 0),
  'U': (0, 1),
  'D': (0, -1),
}

def solve(inp):
  H = (0, 0)
  T = (0, 0)
  Ts = set([(0, 0)])

  for l in inp:
    d, c = l.split(' ')
    dx, dy = DIRS[d]
    for _ in range(int(c)):
      nH = (H[0] + dx, H[1] + dy)
      if nH[0] - T[0] > 1:  # R
        T = (nH[0] - 1, nH[1])
      elif nH[0] - T[0] < -1:  # L
        T = (nH[0] + 1, nH[1])
      if nH[1] - T[1] > 1:  # U
        T = (nH[0], nH[1] - 1)
      if nH[1] - T[1] < -1:  # D
        T = (nH[0], nH[1] + 1)

      H = nH
      Ts.add(T)

  p1 = len(Ts)
  print(f'p1: {p1}')

if __name__ == '__main__':
  solve_input()
