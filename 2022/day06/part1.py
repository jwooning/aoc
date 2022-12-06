#!/usr/bin/env python

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean[0])

def solve(inp):
  p1 = find(inp, 4)
  print(f'p1: {p1}')
  p2 = find(inp, 14)
  print(f'p2: {p2}')


def find(inp, llen):
  buff = [inp[0]] * llen
  c = 0
  for i, ch in enumerate(inp):
    buff[c] = ch

    if len(set(buff)) == llen:
      return i + 1

    c = (c +  1) % llen

if __name__ == '__main__':
  solve_input()
