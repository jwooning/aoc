#!/usr/bin/env python

from collections import deque
from collections import defaultdict

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def find_path(rooms, f, d):
  q = deque([(f, [f], 0)])  # curr, vstd, res
  while len(q):
    curr, vstd, res = q.popleft()

    if curr == d:
      return res

    for n in rooms[curr][1]:
      if n not in vstd:
        q.append((n, vstd + [n], res+1))

  raise ValueError('no path')

def solve(inp):
  rooms = {}
  for l in inp:
    _, room, _, _, rate, _, _, _, _, *lead = l.split(' ')
    rate = int(rate[5:-1])
    lead = [x[:2] for x in lead]
    rooms[room] = (rate, lead)

  valid_rooms = ['AA'] + [room for room, (rate, _) in rooms.items() if rate > 0]
  room_dists = defaultdict(lambda: {})
  for r1 in valid_rooms:
    for r2 in valid_rooms:
      if r1 != r2:
        room_dists[r1][r2] = find_path(rooms, r1, r2)

  q = deque([('AA', ['AA'], 0, 0)])  # room, open, min, res
  p1 = 0
  while len(q):
    room, opn, mins, res = q.popleft()

    if mins > 30:
      continue
    else:
      p1 = max(p1, res)

    for r2 in valid_rooms:
      if r2 not in opn:
        dist = room_dists[room][r2] + 1
        nres = res + (sum([rooms[x][0] for x in opn]) * dist)
        q.append((r2, opn + [r2], mins + dist, nres))

    dist = 30 - mins
    nres = res + (sum([rooms[x][0] for x in opn]) * dist)
    p1 = max(p1, nres)

  print(f'p1: {p1}')

if __name__ == '__main__':
  # solve(['V AA h f rate=0; t l t v DD, II, BB', 'V BB h f rate=13; t l t v CC, AA', 'V CC h f rate=2; t l t v DD, BB', 'V DD h f rate=20; t l t v CC, AA, EE', 'V EE h f rate=3; t l t v FF, DD', 'V FF h f rate=0; t l t v EE, GG', 'V GG h f rate=0; t l t v FF, HH', 'V HH h f rate=22; t l t v GG', 'V II h f rate=0; t l t v AA, JJ', 'V JJ h f rate=21; t l t v II'])
  solve_input()
