#!/usr/bin/env python

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  rocks = set()
  ymax = float('-inf')
  for l in inp:
    for i, coord in enumerate(l.split(' -> ')):
      x, y = coord.split(',')
      x, y = int(x), int(y)

      rocks.add((x, y))
      ymax = max(ymax, y)

      if i == 0:
        px, py = x, y
        continue

      while px != x or py != y:
        if px < x:
          px += 1
        elif px > x:
          px -= 1
        elif py < y:
          py += 1
        elif py > y:
          py -= 1
        else:
          raise Exception(':(')

        rocks.add((px, py))

  done = False
  p2 = 0
  while not done:
    x = 500
    y = 0
    while True:
      at_floor = (y == ymax + 1)
      if not at_floor and (x, y+1) not in rocks:
        y += 1
      elif not at_floor and (x-1, y+1) not in rocks:
        x -= 1
        y += 1
      elif not at_floor and (x+1, y+1) not in rocks:
        x += 1
        y += 1
      else:
        if x == 500 and y == 0:
          done = True
        rocks.add((x, y))
        p2 += 1
        break

  print(f'p2: {p2}')

if __name__ == '__main__':
  # solve(['498,4 -> 498,6 -> 496,6', '503,4 -> 502,4 -> 502,9 -> 494,9'])
  solve_input()
