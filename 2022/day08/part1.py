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
  
  for y in range(forest.shape[1]):
    tallest = -1
    for x in range(forest.shape[0]):
      if forest[y][x] > tallest:
        res.add((y, x))
        tallest = forest[y][x]

    tallest = -1
    for x in range(forest.shape[0]-1, -1, -1):
      if forest[y][x] > tallest:
        res.add((y, x))
        tallest = forest[y][x]

  for x in range(forest.shape[0]):
    tallest = -1
    for y in range(forest.shape[1]):
      if forest[y][x] > tallest:
        res.add((y, x))
        tallest = forest[y][x]

    tallest = -1
    for y in range(forest.shape[1]-1, -1, -1):
      if forest[y][x] > tallest:
        res.add((y, x))
        tallest = forest[y][x]

  p1 = len(res)
  print(f'p1: {p1}')

if __name__ == '__main__':
  # solve(['30373', '25512', '65332', '33549', '35390'])
  solve_input()
