#!/usr/bin/env python

import typing
import itertools
import collections

class Range:
  def __init__(self, _s, _l):
    self.s = _s
    self.l = _l

  @property
  def e(self):
    return self.s + self.l - 1

  def __str__(self):
    return f'Range({self.s} -({self.l})> {self.e})'

  # return pair: new, [old]
  def translate(self, src, dstart):
    if self.e < src.s or self.s > src.e:  # no overlap
      return None, [Range(self.s, self.l)]

    if self.s >= src.s and self.e <= src.e:  # self falls within src
      # print('1')
      return Range(self.s + dstart, self.l), []

    elif self.s == src.s:  # src starts at self and ends within
      # print('2')
      return Range(self.s + dstart, src.l), [Range(src.e, self.l - src.l)]

    elif self.e == src.e:  # src starts within self and ends at self
      # print('3')
      return Range(src.s + dstart, src.l), [Range(self.s, self.l - src.l)]

    elif self.s <= src.s and self.e >= src.e:  # src falls within self
      # print('4')
      return Range(src.s + dstart, src.l), [Range(self.s, src.s - self.s), Range(src.e, self.e - src.s)]

    elif src.s <= self.s < src.e:  # self starts between src
      # print('5')
      return Range(self.s + dstart, src.e - self.s), [Range(src.e + 1, self.e - src.e)]

    else:  # self ends between src
      # print('6')
      return Range(src.s + dstart, self.e - src.s), [Range(self.e + 1, src.e - self.e)]

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  name = None
  ranges = []
  dst_name = None
  dst_ranges = []

  for l in inp:
    if l.startswith('seeds:'):
      name = 'seed'

      seeds = [int(x) for x in l.split()[1:]]
      for i in range(0, len(seeds), 2):
        ranges.append(Range(seeds[i], seeds[i+1]))

    elif l.endswith('map:'):
      src_name, dst_name = l.split()[0].split('-to-')
      assert src_name == name

    elif len(l):
      dst_start, src_start, range_len = [int(x) for x in l.split()]
      src_range = Range(src_start, range_len)

      new_ranges = []
      for r in list(ranges):
        new, olds = r.translate(src_range, dst_start - src_start)

        if new is not None:
          dst_ranges.append(new)

        new_ranges += olds

        print(str(r), str(src_range), dst_start - src_start, '-->', str(new), [str(x) for x in olds])
      ranges = new_ranges

    elif dst_name is not None:
      name = dst_name
      ranges += dst_ranges
      dst_name = None
      dst_ranges = []

      print(name)
      print([(r.s, r.l) for r in ranges])
      print('---')

  name = dst_name
  ranges += dst_ranges
  dst_name = None
  dst_ranges = []

  assert name == 'location'

  p2 = sorted([r.s for r in ranges])[0]

  print(f'p2: {p2}')

if __name__ == '__main__':
  # solve(['seeds: 79 14 55 13', '', 'seed-to-soil map:', '50 98 2', '52 50 48', '', 'soil-to-fertilizer map:', '0 15 37', '37 52 2', '39 0 15', '', 'fertilizer-to-water map:', '49 53 8', '0 11 42', '42 0 7', '57 7 4', '', 'water-to-light map:', '88 18 7', '18 25 70', '', 'light-to-temperature map:', '45 77 23', '81 45 19', '68 64 13', '', 'temperature-to-humidity map:', '0 69 1', '1 0 69', '', 'humidity-to-location map:', '60 56 37', '56 93 4'])
  solve_input()
