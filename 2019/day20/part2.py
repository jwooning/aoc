#!/usr/bin/env python

from collections import defaultdict

def solve_input(file):
  with open(file, 'r') as f:
    file_content = f.read()
    solve(file_content)

def find(m, needle):
  res = np.where(m == needle)
  return res[0][0], res[1][0]

def solve(inp):
  m = []
  for line in inp.split('\n'):
    if len(line):
      m.append([char for char in line])

  labels = defaultdict(lambda: [])
  for i in range(1, len(m) - 1):
    for j in range(1, len(m[0]) - 1):
      if m[i][j].isupper():
        if m[i][j+1].isupper() and m[i][j-1] == '.':
          labels[m[i][j] + m[i][j+1]].append((i, j-1))
        elif m[i][j-1].isupper() and m[i][j+1] == '.':
          labels[m[i][j-1] + m[i][j]].append((i, j+1))
        elif m[i+1][j].isupper() and m[i-1][j] == '.':
          labels[m[i][j] + m[i+1][j]].append((i-1, j))
        elif m[i-1][j].isupper() and m[i+1][j] == '.':
          labels[m[i-1][j] + m[i][j]].append((i+1, j))

  o_ps = {}  # in to out
  i_ps = {}  # out to in
  start = None
  end = None
  for l, poss in labels.items():
    if l == 'AA':
      assert len(poss) == 1
      y, x = poss[0]
      start = (0, y, x)
    elif l == 'ZZ':
      assert len(poss) == 1
      y, x = poss[0]
      end = (0, y, x)
    else:
      assert len(poss) == 2
      if poss[0][0] in [2, len(m) - 3] or poss[0][1] in [2, len(m[0]) - 3]:
        o_ps[poss[0]] = poss[1]
        i_ps[poss[1]] = poss[0]
      else:
        i_ps[poss[0]] = poss[1]
        o_ps[poss[1]] = poss[0]

  todo = [(start, 0, frozenset([start]))]  # curr, l, visited
  hist = {}
  while len(todo):
    curr, l, vstd = todo.pop(0)

    if curr == end:
      print(f'p2: {l}')
      break

    if curr in hist and l >= hist[curr]:
      continue

    hist[curr] = l

    level, y, x = curr
    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
      ny = y + dy
      nx = x + dx
      if m[ny][nx] == '.' and m[ny][nx] not in vstd:
        nvstd = vstd | frozenset([(ny, nx)])
        todo.append(((level, ny, nx), l + 1, nvstd))

    if (y, x) in o_ps and level > 0:
      ny, nx = o_ps[(y, x)]
      if (level - 1, ny, nx) not in vstd:
        nvstd = vstd | frozenset([(level - 1, ny, nx)])
        todo.append(((level - 1, ny, nx), l + 1, nvstd))

    if (y, x) in i_ps:
      ny, nx = i_ps[(y, x)]
      if (level + 1, ny, nx) not in vstd:
        nvstd = vstd | frozenset([(level + 1, ny, nx)])
        todo.append(((level + 1, ny, nx), l + 1, nvstd))

if __name__ == '__main__':
  solve_input('input')
