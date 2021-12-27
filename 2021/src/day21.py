#!/usr/bin/env python
import os
import sys
import struct
import copy
import math
import time
import itertools
import collections
import uuid

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  lines = [x for x in in_ if x]
  pos = [int(l.split('starting position: ')[1]) for l in lines]
  p1 = game_p1(pos.copy())
  print(f'p1: {p1}')
  p2 = game_p2(pos.copy())
  print(f'p2: {p2}')

def game_p2(pos):
  mults = collections.defaultdict(lambda: 0)
  for dies in itertools.product(range(1, 4), range(1, 4), range(1, 4)):
    mults[sum(dies)] += 1

  wins = [0, 0]
  q = collections.deque([])
  for s, m in mults.items():
    q.append((0, s, m, tuple(pos), (0, 0)))
    player, roll, mult, pos, scores = q.popleft()

    if player == 0:
      pos = (pos[0] + roll, pos[1])
      while pos[0] > 10:
        pos = (pos[0] - 10, pos[1])
      scores = (scores[0] + pos[0], scores[1])
    else:
      pos = (pos[0], pos[1] + roll)
      while pos[1] > 10:
        pos = (pos[0], pos[1] - 10)
      scores = (scores[0], scores[1] + pos[1])

    if scores[0] >= 21:
      wins[0] += mult
    elif scores[1] >= 21:
      wins[1] += mult
    else:
      for s, m in mults.items():
        q.append((1 - player, s, mult * m, pos, scores))

  return max(wins)

def game_p1(pos):
  player = 0
  die = 0
  scores = [0, 0]
  rolls = 0
  while True:
    roll = 0
    for _ in range(3):
      die += 1
      if die > 100:
        die = 1
      roll += die

    pos[player] += roll
    while pos[player] > 10:
      pos[player] -= 10

    scores[player] += pos[player]

    player = 1 - player
    rolls += 3
    if scores[0] >= 1000 or scores[1] >= 1000:
       p1 = min(scores) * rolls
       return p1

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_)
