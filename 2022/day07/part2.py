#!/usr/bin/env python

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

class Dir:
  def __init__(self, p):
    self.parent = p
    self.children = {}

  def put(self, n, c):
    self.children[n] = c

  def get(self, n):
    return self.children.get(n)

  def size(self):
    return sum([c.size() for c in self.children.values()])

class File:
  def __init__(self, n, s):
    self._size = s

  def size(self):
    return self._size

def solve(inp):
  root = Dir(None)
  cwd = None
  for l in inp:
    print(l)
    if l.startswith('$ cd '):
      dir_ = l[5:]
      if dir_ == '/':
        cwd = root
      elif dir_ == '..':
        cwd = cwd.parent
      else:
        assert cwd.get(dir_) is not None
        cwd = cwd.get(dir_)

    elif l.startswith('$ ls'):
      pass

    elif l.startswith('dir '):
      dir_ = l[4:]
      assert cwd.get(dir_) is None
      cwd.put(dir_, Dir(cwd))

    else:
      s, n = l.split(' ')
      assert cwd.get(n) is None
      cwd.put(n, File(n, int(s)))

  def smallest(dir_, to_del):
    res = int(10e10)
    if dir_.size() > to_del:
      res = dir_.size()

    for c in dir_.children.values():
      if isinstance(c, Dir):
        res = min(smallest(c, to_del), res)

    return res

  p2 = smallest(root, root.size() - (70000000 - 30000000))
  print(f'p2: {p2}')

if __name__ == '__main__':
  solve_input()
