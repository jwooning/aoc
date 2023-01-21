#!/usr/bin/env python

from collections import defaultdict

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def dist(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve(inp):
  m = 4000000

  ys = defaultdict(lambda: [])

  for j, l in enumerate(inp):
    l = ''.join([x for x in l if x in '-0123456789:,'])
    sens, beac = l.split(':')
    sens = tuple([int(x) for x in sens.split(',')])
    beac = tuple([int(x) for x in beac.split(',')])

    d = dist(sens, beac)

    for i in range(max(0, sens[0] - d), min(m, sens[0] + d) + 1):
      l = d - abs(sens[0] - i)
      ys[i].append(range(max(0, sens[1] - l), min(m, sens[1] + l) + 1))

    print(f'{j}/{len(inp)}')

  print('half')

  for i in range(m+1):
    if i % 1000 == 0:
      print(f'{i/1000}/{m/1000}')

    yrs = sorted(ys[i], key=lambda x: x.start)
    x = 0
    done = False
    while len(yrs):
      r = yrs.pop(0)
      if x < r.start:
        done = True
        break

      if r.stop > x:
        x = r.stop

    if x < m or done:
      break

  p2 = i * 4000000 + x
  print(f'p2: {p2}')

if __name__ == '__main__':
  # solve(['2,18:-2,15', '9,16:10,16', '13,2:15,3', '12,14:10,16', '10,20:10,16', '14,17:10,16', '8,7:2,10', '2,0:2,10', '0,11:2,10', '20,14:25,17', '17,20:21,22', '16,7:15,3', '14,3:15,3', '20,1:15,3'])
  solve_input()
