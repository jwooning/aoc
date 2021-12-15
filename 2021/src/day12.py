#!/usr/bin/env python
import os
import sys
import struct
import copy
import itertools
import collections

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  lines = [x for x in in_ if x]
  edges = set()
  for l in lines:
    s, e = l.split('-')
    edges.update({(s, e), (e, s)})

  p1 = 0
  todo = collections.deque([(set(), 'start')])
  while len(todo):
    visited, at = todo.popleft()
    if at.lower() == at:
      visited.add(at)

    if at == 'end':
      p1 += 1
      continue

    for s, e in edges:
      if s == at and e not in visited:
        todo.append((visited.copy(), e))

  print(f'p1: {p1}')

  p2 = 0
  todo = collections.deque([(set(), 'start')])
  while len(todo):
    visited, at = todo.popleft()
    if at.lower() == at:
      if at in visited:
        visited.add('!!!')
      else:
        visited.add(at)

    if at == 'end':
      p2 += 1
      continue

    for s, e in edges:
      if s == at and e != 'start' and (e not in visited or '!!!' not in visited):
        todo.append((copy.copy(visited), e))

  print(f'p2: {p2}')


if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  run(input_)
