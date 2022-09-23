#!/usr/bin/env python

import copy
import numpy as np
from collections import OrderedDict
from collections import defaultdict

class Graph:
  def __init__(self):
    self.nodes = {}

  def __getitem__(self, id_):
    if id_ not in self.nodes:
      self.nodes[id_] = Node(id_)

    return self.nodes[id_]

  def parse(self, m):
    todo = []

    for y, l in enumerate(m):
      for x, ch in enumerate(l):
        if ch == b'@' or ch.islower():
          todo.append((y, x, ch, 0, set(), set([(y, x)])))  # y, x, id_, length, doors, visited

    while len(todo):
      y, x, id_, l, drs, vstd = todo.pop(0)
      for dy, dx in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        ny = y + dy
        nx = x + dx
        if (ny, nx) in vstd:
          continue
        if m[ny, nx] == b'#':
          continue
        elif m[ny, nx] == b'@' or m[ny, nx].islower():
          self[id_].add_edge(self[m[ny, nx]], Edge(l + 1, drs))
          continue

        ndrs = drs.copy()
        nvstd = vstd.copy()

        nvstd.add((ny, nx))
        if m[ny][nx].isupper():
          ndrs.add(m[ny, nx].lower())

        todo.append((ny, nx, id_, l + 1, ndrs, nvstd))

class Node:
  def __init__(self, id_):
    self.id_ = id_
    self.edges = defaultdict(lambda: [])

  def add_edge(self, n, e):
    if e not in self.edges[n.id_]:
      self.edges[n.id_].append(e)
      self.edges[n.id_] = sorted(self.edges[n.id_], key=lambda x: x.w)

      n.edges[self.id_].append(e)
      n.edges[self.id_] = sorted(n.edges[self.id_], key=lambda x: x.w)

  def __str__(self):
    return f'N({self.id_})'

class Edge:
  def __init__(self, w, doors):
    self.w = w
    self.doors = frozenset(doors)

  def __eq__(self, o):
    return self.w == o.w and self.doors == o.doors

  def __str__(self):
    return f'E({self.w}, {self.doors})'

def solve_input(file):
  with open(file, 'r') as f:
    file_content = f.read().strip()
    solve(file_content)

def find(m, needle):
  res = np.where(m == needle)
  return res[0][0], res[1][0]

def solve(inp):
  all_keys = frozenset()
  MAP = []
  for line in inp.split('\n'):
    MAP.append([char for char in line])
    all_keys |= frozenset([char for char in line if char.islower() and char.isalpha()])

  m = np.chararray((len(MAP), len(MAP[0])))
  m[:] = MAP

  Y, X = find(m, b'@')

  m[Y-1, X-1: X+2] = [b'@', b'#', b'@']
  m[Y+0, X-1: X+2] = [b'#', b'#', b'#']
  m[Y+1, X-1: X+2] = [b'@', b'#', b'@']

  ms = []
  ms.append(m[:Y+1, :X+1])
  ms.append(m[:Y+1, X:])
  ms.append(m[Y:, :X+1])
  ms.append(m[Y:, X:])

  graphs = []
  for m in ms:
    g = Graph()
    g.parse(m)
    graphs.append(g)


  history = {}
  todo = [((b'@', b'@', b'@', b'@'), 0, frozenset())]
  res = None
  while len(todo):
    ats, steps, keys = todo.pop(0)

    if len(keys) == len(all_keys):
      res = steps if res is None else min(res, steps)
      continue

    for i in range(4):
      at = ats[i]
      g = graphs[i]

      for nat, es in g[at].edges.items():
        for e in es:
          if e.doors.issubset(keys):
            nats = list(ats)
            nats[i] = nat
            nats = tuple(nats)
            if nat == b'@':
              nkeys = keys.copy()
            else:
              nkeys = keys | frozenset([nat])

            print(len(nkeys), len(all_keys), nats, steps + e.w, sorted(list(nkeys)))
            if (nats, nkeys) not in history or history[(nats, nkeys)] > steps + e.w:
              history[(nats, nkeys)] = steps + e.w
              todo.append((nats, steps + e.w, nkeys))

  print(f'p2: {res}')

if __name__ == '__main__':
  # solve_input('input_t1')
  solve_input('input')
