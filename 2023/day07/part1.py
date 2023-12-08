#!/usr/bin/env python

import itertools
import collections
import functools

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def getTypeScore(h):
  cnt = {c: 0 for c in cards}
  for c in h:
    cnt[c] += 1

  cnt_srt = sorted(cnt.values(), reverse=True)

  if cnt_srt[0] == 5:
    return 6
  elif cnt_srt[0] == 4:
    return 5
  elif cnt_srt[0] == 3 and cnt_srt[1] == 2:
    return 4
  elif cnt_srt[0] == 3:
    return 3
  elif cnt_srt[0] == 2 and cnt_srt[1] == 2:
    return 2
  elif cnt_srt[0] == 2:
    return 1
  else:
    return 0

def order(l1, l2):
  h1 = l1[0]
  h2 = l2[0]

  ts1 = getTypeScore(h1)
  ts2 = getTypeScore(h2)

  if ts1 != ts2:
    return ts1 - ts2

  for i in range(5):
    cs1 = len(cards) - cards.index(h1[i])
    cs2 = len(cards) - cards.index(h2[i])

    if cs1 != cs2:
      return cs1 - cs2

  print(h1, ts1, cs1, h2, ts1, cs2)

def solve(inp):
  p1 = 0
  hands = [l.split() for l in inp]

  hands.sort(key=functools.cmp_to_key(order))
  for rank, (_, val) in enumerate(hands):
    p1 += (rank + 1) * int(val)

  print(f'p1: {p1}')

if __name__ == '__main__':
  solve_input()
