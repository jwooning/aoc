#!/usr/bin/env python

import numpy as np

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  res = set()
  forest = np.array([[int(x) for x in y] for y in inp], dtype=np.uint8)

  views = np.ones(forest.shape, dtype=np.uint)

  for y in range(forest.shape[1]):
    view = [0] * 10
    for x in range(forest.shape[0]):
      views[y][x] *= view[forest[y][x]]
      for i in range(10):
        if forest[y][x] >= i:
          view[i] = 1
        else:
          view[i] += 1

    view = [0] * 10
    for x in range(forest.shape[0]-1, -1, -1):
      views[y][x] *= view[forest[y][x]]
      for i in range(10):
        if forest[y][x] >= i:
          view[i] = 1
        else:
          view[i] += 1

  for x in range(forest.shape[0]):
    view = [0] * 10
    for y in range(forest.shape[1]):
      views[y][x] *= view[forest[y][x]]
      for i in range(10):
        if forest[y][x] >= i:
          view[i] = 1
        else:
          view[i] += 1

    view = [0] * 10
    for y in range(forest.shape[1]-1, -1, -1):
      views[y][x] *= view[forest[y][x]]
      for i in range(10):
        if forest[y][x] >= i:
          view[i] = 1
        else:
          view[i] += 1

  p2 = np.max(views)
  print(f'p2: {p2}')

if __name__ == '__main__':
  # solve(['30373', '25512', '65332', '33549', '35390'])
  solve_input()
