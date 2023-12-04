#!/usr/bin/env python

import itertools
import collections

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  p1 = 0
  p2 = 0

  copies = collections.defaultdict(lambda: 1)

  for l in inp:
    card_num, game = [x.strip() for x in l.split(':')]
    card_num = int(card_num.split()[-1])
    if card_num not in copies:
      copies[card_num] = 1
    game_win, game_me = [x.strip() for x in game.split('|')]
    win_nums = [int(x) for x in game_win.split()]
    nums = [int(x) for x in game_me.split()]

    points = 0
    i = 0
    for num in nums:
      if num in win_nums:
        if points == 0:
          points = 1
        else:
          points *= 2

        i += 1
        copies[card_num + i] += copies[card_num]

    p1 += points

  p2 = sum(copies.values())

  print(f'p1: {p1}')
  print(f'p2: {p2}')

if __name__ == '__main__':
  # solve(['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53', 'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19', 'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1', 'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83', 'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36', 'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'])
  solve_input()
