import sys
import math
import collections
import itertools
import functools
import struct
import time

import numpy as np

def read_input(path):
    with open(path, 'r') as f:
        return f.read().split('\n')

def parse_input(lines):
    return [l.strip() for l in lines if len(l)]

def run(inp):
    black = set()
    for line in inp:
        coord = locate(line)
        if coord not in black:
            black.add(coord)
        else:
            black.remove(coord)

    print('p1: {}'.format(len(black)))

    for i in range(100):
        ngbrs = {}
        for x, y in black:
            for xa, ya in [(1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)]:
                coord = (x + xa, y + ya)
                if coord not in ngbrs:
                    ngbrs[coord] = 0
                ngbrs[coord] += 1

        new_black = set()
        for coord, count in ngbrs.items():
            if coord in black and (count == 1 or count == 2):
                new_black.add(coord)
            elif coord not in black and count == 2:
                new_black.add(coord)

        black = new_black

        if i + 1 in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
            print('p2: {} ({})'.format(len(black), i))

def locate(line):
    i = 0
    x = 0
    y = 0
    while i < len(line):
        ch = line[i]
        if ch == 'n' or ch == 's':
            i += 1
            ch += line[i]

        if ch == 'e':
            x += 1
        elif ch == 'se':
            x += 1
            y -= 1
        elif ch == 'sw':
            y -= 1
        elif ch == 'w':
            x -= 1
        elif ch == 'nw':
            x -= 1
            y += 1
        elif ch == 'ne':
            y += 1

        i += 1


    return x, y

if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    inp = parse_input(input_)
    run("""sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew""".split('\n'))
    run(inp)
