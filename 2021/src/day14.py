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
  template = None

  rules = {}
  for l in lines:
    if template is None:
      template = l
      continue

    a, b = l.split(' -> ')
    rules[a] = [a[0] + b, b + a[1]]

  counts = collections.defaultdict(lambda: 0)
  for i in range(len(template) - 1):
    counts[template[i:i+2]] += 1


  for j in range(40):
    new_counts = collections.defaultdict(lambda: 0)

    for t, c in counts.items():
      if t in rules:
        ta, tb = rules[t]
        new_counts[ta] += c
        new_counts[tb] += c
      else:
        new_counts[t] += c

    counts = new_counts

    if j in [9, 39]:
      cc = collections.defaultdict(lambda: 0)
      cc[template[-1]] += 1
      for t, c in counts.items():
        cc[t[0]] += c

      res = max(cc.values()) - min(cc.values())
      print(f'{j+1}: {res}')

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  #input_ = ['NNCB', 'CH -> B', 'HH -> N', 'CB -> H', 'NH -> C', 'HB -> C', 'HC -> B', 'HN -> C', 'NN -> C', 'BH -> H', 'NC -> B', 'NB -> B', 'BN -> B', 'BB -> N', 'BC -> B', 'CC -> N', 'CN -> C']
  run(input_)
