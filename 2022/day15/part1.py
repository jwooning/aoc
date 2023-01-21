#!/usr/bin/env python

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def dist(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve(inp):
  y = 2000000
  # y = 10
  xs = set()
  not_xs = set()

  for l in inp:
    l = ''.join([x for x in l if x in '-0123456789:,'])
    sens, beac = l.split(':')
    sens = tuple([int(x) for x in sens.split(',')])
    beac = tuple([int(x) for x in beac.split(',')])

    if beac[1] == y:
      not_xs.add(beac[0])

    d = dist(sens, beac)
    dy = abs(sens[1] - y)

    dx = d - dy
    if dx >= 0:
      for i in range(sens[0] - dx, sens[0] + dx + 1):
        xs.add(i)

  p1 = len(xs - not_xs)
  print(f'p1: {p1}')

if __name__ == '__main__':
  # solve(['2,18:-2,15', '9,16:10,16', '13,2:15,3', '12,14:10,16', '10,20:10,16', '14,17:10,16', '8,7:2,10', '2,0:2,10', '0,11:2,10', '20,14:25,17', '17,20:21,22', '16,7:15,3', '14,3:15,3', '20,1:15,3'])
  solve_input()
