#!/usr/bin/env python
import os
import sys
import struct
import itertools
from collections import defaultdict

open_ = {'(': ')', '[': ']', '{': '}', '<': '>'}
close = {')': 0, ']': 1, '}': 2, '>': 3}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
score = {'(': 1, '[': 2, '{': 3, '<': 4}
close = ['()', '[]', '{}', '<>']

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  lines = [x for x in in_ if x]

  p1 = 0
  scores = []
  for l in lines:
    cont = True
    while cont:
      cont = False
      for c in close:
        if c in l:
          cont = True
          idx = l.index(c)
          l = l[0:idx] + l[idx+2:]

    for ch in l:
      if ch in points:
        p1 += points[ch]
        break
    else:
      sc = 0
      for ch in l[::-1]:
        sc = (sc * 5) + score[ch]

      scores.append(sc)

  p2 = sorted(scores)[len(scores)//2]

  print(f'p1: {p1}')
  print(f'p2: {p2}')

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  #input_ = ['[({(<(())[]>[[{[]{<()<>>', '[(()[<>])]({[<{<<[]>>(', '{([(<{}[<>[]}>{[]{[(<()>', '(((({<>}<{<{<>}{[]{[]{}', '[[<[([]))<([[{}[[()]]]', '[{[{({}]{}}([{[{{{}}([]', '{<[[]]>}<{[{[{[]{()[[[]', '[<(<(<(<{}))><([]([]()', '<{([([[(<>()){}]>(<<{{', '<{([{{}}[<[[[<>{}]]]>[]]']
  run(input_)
