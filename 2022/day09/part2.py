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
  S = [(0, 0)] * 10
  Ts = set([(0, 0)])

  for l in inp:
    d, c = l.split(' ')
    dx, dy = DIRS[d]

    for _ in range(int(c)):
      nS = [(S[0][0] + dx, S[0][1] + dy)]

      for i in range(1, 10):
        if nS[i-1][0] - S[i][0] > 1 and nS[i-1][1] - S[i][1] > 1:  # RU
          T = (nS[i-1][0] - 1, nS[i-1][1] - 1)
        elif nS[i-1][0] - S[i][0] > 1 and nS[i-1][1] - S[i][1] < -1:  # RD
          T = (nS[i-1][0] - 1, nS[i-1][1] + 1)
        elif nS[i-1][0] - S[i][0] < -1 and nS[i-1][1] - S[i][1] < -1:  # LD
          T = (nS[i-1][0] + 1, nS[i-1][1] + 1)
        elif nS[i-1][0] - S[i][0] < -1 and nS[i-1][1] - S[i][1] > 1:  # LU
          T = (nS[i-1][0] + 1, nS[i-1][1] - 1)
        elif nS[i-1][0] - S[i][0] > 1:  # R
          T = (nS[i-1][0] - 1, nS[i-1][1])
        elif nS[i-1][0] - S[i][0] < -1:  # L
          T = (nS[i-1][0] + 1, nS[i-1][1])
        elif nS[i-1][1] - S[i][1] > 1:  # U
          T = (nS[i-1][0], nS[i-1][1] - 1)
        elif nS[i-1][1] - S[i][1] < -1:  # D
          T = (nS[i-1][0], nS[i-1][1] + 1)
        else:
          T = (S[i][0], S[i][1])

        nS.append(T)

      S = nS
      Ts.add(S[-1])

  p2 = len(Ts)
  print(f'p2: {p2}')

if __name__ == '__main__':
  # solve(['R 4', 'U 4'])
  solve_input()
