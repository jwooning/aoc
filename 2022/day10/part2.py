#!/usr/bin/env python

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  p2 = []
  X = 1
  ip = 0
  adding = False

  for i in range(1, 241):
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

    p = (i-1) % 40
    if abs(X - p) <= 1:
      p2.append('#')
    else:
      p2.append('.')

    X += dX

    if i % 40 == 0:
      print(''.join(p2))
      p2 = []

if __name__ == '__main__':
  solve_input()
