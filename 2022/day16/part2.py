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
  valid_rooms = sorted(valid_rooms, key=lambda x: rooms[x][0], reverse=True)
  room_dists = defaultdict(lambda: {})
  for r1 in valid_rooms:
    for r2 in valid_rooms:
      if r1 != r2:
        room_dists[r1][r2] = find_path(rooms, r1, r2)

  q = deque([('AA', 'AA', 0, ['AA'], 0, 0)])  # r1, r2, rem2, open, min, res
  p2 = 0
  hist = {}
  while len(q):
    if len(q) % 10000 == 0:
      print(len(q))
    r1, r2, rem2, opn, mins, res = q.popleft()

    nres = res
    nres += (sum([rooms[x][0] for x in opn if x != r2]) * rem2)
    nres += (sum([rooms[x][0] for x in opn]) * (26 - mins - rem2))
    if nres > p2:
      p2 = nres
      print(p2)

    nrooms = [x for x in valid_rooms if x not in opn]
    for d1 in nrooms:
      dst1 = room_dists[r1][d1] + 1
      dist = min(dst1, rem2)
      nropn = [rooms[x][0] for x in opn if x != r2 or rem2 == 0]
      nres = res + (sum(nropn) * dist)

      nr1 = d1
      nrem1 = dst1 - dist
      nr2 = r2
      nrem2 = rem2 - dist
      if nrem1 != 0:
        nr1, nr2 = nr2, nr1
        nrem1, nrem2 = nrem2, nrem1

      nopn = sorted(opn + [d1])
      hh = (nrem2, tuple(sorted(nropn)), mins + dist)
      if mins + dist <= 26 and (hh not in hist or nres > hist[hh]):
        hist[hh] = nres
        q.append((nr1, nr2, nrem2, nopn, mins + dist, nres))

  print(f'p2: {p2}')

if __name__ == '__main__':
  solve(['V AA h f rate=0; t l t v DD, II, BB', 'V BB h f rate=13; t l t v CC, AA', 'V CC h f rate=2; t l t v DD, BB', 'V DD h f rate=20; t l t v CC, AA, EE', 'V EE h f rate=3; t l t v FF, DD', 'V FF h f rate=0; t l t v EE, GG', 'V GG h f rate=0; t l t v FF, HH', 'V HH h f rate=22; t l t v GG', 'V II h f rate=0; t l t v AA, JJ', 'V JJ h f rate=21; t l t v II'])
  solve_input()
