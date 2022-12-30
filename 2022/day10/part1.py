#!/usr/bin/env python

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  p1 = 0
  X = 1
  ip = 0
  adding = False

  for i in range(1, 221):
    l = inp[ip]
    dX = 0

    if l.startswith('addx'):
      if not adding:
        adding = True
      else:
        _, c = l.split(' ')
        dX = int(c)
        adding = False
        ip += 1
    elif l == 'noop':
      ip += 1

    if i in [20, 60, 100, 140, 180, 220]:
      p1 += i * X

    X += dX

  print(f'p1: {p1}')

if __name__ == '__main__':
  # solve(['noop', 'addx 3', 'addx -5'])
  solve_input()
