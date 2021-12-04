#!/usr/bin/env python
import os
import sys
import struct

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  numbers = [int(x) for x in next(in_).split(',')]

  boards = []
  board = None
  for l in in_:
    if not l:
      if board:
        boards.append(board)
      board = ([], [0] * 5, [0] * 5)
      j = 0
      continue

    line = [int(x) for x in l.split(' ') if x]
    board[0].extend([(x, i, j) for i, x in enumerate(line)])
    j += 1

  bingoed = []
  for i, n in enumerate(numbers):
    for j, (board, rows, cols) in enumerate(boards):
      for x, r, c in board:
        if x == n:
          rows[r] += 1
          cols[c] += 1

      if j not in bingoed and (5 in rows or 5 in cols):
        bingoed.append(j)
        if len(bingoed) == 1 or len(bingoed) == len(boards):
          print('bingo!')
          sum_ = 0
          for x, _, _ in board:
            if x not in numbers[:i+1]:
              sum_ += x

          print(f'p: {sum_}*{n} = {sum_*n}')

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_)
