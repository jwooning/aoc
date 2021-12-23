#!/usr/bin/env python
import os
import sys
import struct
import copy
import time
import math
import itertools
import collections

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  lines = [x for x in in_ if x]
  nums = [eval(x) for x in lines]
  root = Node.create(nums[0])
  reduce(root)
  for n in nums[1:]:
    node = Node.create(n)
    new_root = Node(None)
    new_root.l = root
    new_root.r = node
    node.parent = new_root
    root.parent = new_root
    root = new_root
    reduce(root)

  print(root)
  print(magnitude(root))

  p2 = 0
  for a, b in itertools.product(nums, nums):
    l = Node.create(a)
    r = Node.create(b)
    root = Node(None)
    l.parent = root
    r.parent = root
    root.l = l
    root.r = r
    reduce(root)
    p2 = max(p2, magnitude(root))

  print(f'p2: {p2}')

def reduce(root):
  while True:
    exploded = explode(root)
    if exploded:
      continue
  
    splitted = split(root)
    if splitted:
      continue

    return

def explode(node, d=0):
  if node.val is not None:
    return False

  if d == 4:
    l = node.l.val
    r = node.r.val
    node.l = None
    node.r = None
    node.val = 0
    nl = node.bt(left=True)
    if nl:
      nl.val += l
    nr = node.bt(left=False)
    if nr:
      nr.val += r
    return True

  return explode(node.l, d + 1) or explode(node.r, d + 1)

def split(node):
  if node.val is not None and node.val >= 10:
    l = math.floor(node.val / 2)
    r = math.ceil(node.val / 2)
    node.val = None
    node.l = Node(node, l)
    node.r = Node(node, r)
    return True

  if node.val is not None:
    return False

  return split(node.l) or split(node.r)

def magnitude(node):
  if node.val is not None:
    return node.val

  return 3 * magnitude(node.l) + 2 * magnitude(node.r)

class Node:
  @staticmethod
  def create(item, parent=None):
    if type(item) == list:
      res = Node(parent)
      res.l = Node.create(item[0], res)
      res.r = Node.create(item[1], res)
      return res
    else:
      return Node(parent, val=item)

  def __init__(self, parent, val=None):
    self.val = val
    self.parent = parent
    self.l = None
    self.r = None

  def __str__(self):
    if self.val is not None:
      return str(self.val)
    return f'[{self.l},{self.r}]'

  def bt(self, left):
    f = self
    stepped = False
    while True:
      if f is not self and f.val is not None:
        return f
      elif f.parent is None:
        return None
      elif stepped and left:
        f = f.r
      elif stepped and not left:
        f = f.l
      elif left and f.parent.l != f:
        f = f.parent.l
        stepped = True
      elif not left and f.parent.r != f:
        f = f.parent.r
        stepped = True
      else:
        f = f.parent

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  #input_ = ['[1,1]', '[2,2]', '[3,3]', '[4,4]', '[5,5]', '[6,6]']
  #input_ = ['[[[[[9,8],1],2],3],4]']
  #input_ = ['[[[[4,3],4],4],[7,[[8,4],9]]]', '[1,1]']
  #input_ = ['[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]','[[[5,[2,8]],4],[5,[[9,9],0]]]','[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]','[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]','[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]','[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]','[[[[5,4],[7,7]],8],[[8,3],8]]','[[9,3],[[9,9],[6,[4,9]]]]','[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]','[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]']
  #input_ = ['[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]','[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]']#,'[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]','[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]','[7,[5,[[3,8],[1,4]]]]','[[2,[2,2]],[8,[8,1]]]','[2,9]','[1,[[[9,3],9],[[9,0],[0,7]]]]','[[[5,[7,4]],7],1]','[[[[4,2],2],6],[8,7]]']
  #input_ = ['[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]']
  run(input_)
