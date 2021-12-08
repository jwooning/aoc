#!/usr/bin/env python
import os
import sys
import struct
import itertools
from collections import defaultdict

letters = list('abcdefg')
lis = {l: i for i, l in enumerate(letters)}
nums = {
  0: frozenset(['a', 'b', 'c', 'e', 'f', 'g']),
  1: frozenset(['c', 'f']),
  2: frozenset(['a', 'c', 'd', 'e', 'g']),
  3: frozenset(['a', 'c', 'd', 'f', 'g']),
  4: frozenset(['b', 'c', 'd', 'f']),
  5: frozenset(['a', 'b', 'd', 'f', 'g']),
  6: frozenset(['a', 'b', 'd', 'e', 'f', 'g']),
  7: frozenset(['a', 'c', 'f']),
  8: frozenset(['a', 'b', 'c', 'd', 'e', 'f', 'g']),
  9: frozenset(['a', 'b', 'c', 'd', 'f', 'g']),
}
nums_rev = {v: k for k, v in nums.items()}

lens = defaultdict(list)
for num, sigs in nums.items():
  lens[len(sigs)].append(num)

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  lines = [x for x in in_ if x]

  p1 = 0
  for line in lines:
    _, out = [x.split(' ') for x in line.split(' | ')]
    for word in out:
      if len(lens[len(word)]) == 1:
        p1 += 1

  print(f'p1: {p1}')

  p2 = 0
  for line in lines:
    pattern, out = [x.split(' ') for x in line.split(' | ')]
    
    for sol in itertools.permutations(letters, len(letters)):
      cont = False
      for word in pattern:
        combi = frozenset([sol[lis[l]] for l in word])
        if combi not in nums_rev:
          cont = True
          break

      if cont:
        continue

      add = 0
      for i, word in enumerate(out):
        combi = frozenset([sol[lis[l]] for l in word])
        if combi not in nums_rev:
          cont = True
          break

        add += (10**(3 - i)) * nums_rev[combi]

      if cont:
        continue

      p2 += add

    print(f'p2: {p2}')

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_)
