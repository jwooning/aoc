import sys
import math
import collections
import itertools
import functools
import struct
import code

import numpy as np

from matplotlib import pyplot as plt

tiles = {}
tile_edges = {}
tile_matches = {}

def read_input(path):
    with open(path, 'r') as f:
        return f.read().split('\n')

def parse_input(lines):
    return lines

def run(inp):
    global tiles, tile_edges, tile_matches

    size = 10
    for line in inp:
        if line.startswith('Tile '):
            tile = np.zeros((size, size), dtype=np.uint8)
            id_ = int(line[5:-1])
            i = 0
            continue

        if len(line) == 0:
            tiles[id_] = tile
            continue

        for j, ch in enumerate(line):
            if ch == '#':
                tile[j][i] = 1

        i += 1

    for id_, tile in tiles.items():
        tile_edges[id_] = {}  # (r_clockw, xflip, yflip, {top: 0, right: 1, bot: 2, left: 3}): hash

        for i in range(2):
            for xflip, yflip in itertools.product((False, True), repeat=2):
                trans_tile = np.rot90(tile, k=i, axes=(1,0))
                if xflip:
                    trans_tile = np.fliplr(trans_tile)
                if yflip:
                    trans_tile = np.flipud(trans_tile)

                tile_edges[id_][(i, xflip, yflip, 0)] = tuple(trans_tile[:, 0])
                tile_edges[id_][(i, xflip, yflip, 1)] = tuple(trans_tile[size-1, :])
                tile_edges[id_][(i, xflip, yflip, 2)] = tuple(trans_tile[:, size-1])
                tile_edges[id_][(i, xflip, yflip, 3)] = tuple(trans_tile[0, :])

    for id_, edges in tile_edges.items():
        for edge, hash_ in edges.items():
            if hash_ not in tile_matches:
                tile_matches[hash_] = []

            tile_matches[hash_].append((id_, edge))

    at_id = list(tile_edges.keys())[1]
    at_orientation = (0, False, False)
    dirs = [0, 1, 2, 3, 0]
    dir_i = 0
    visited = {at_id,}
    corners = []
    while dir_i < len(dirs):
        dir_ = dirs[dir_i]
        print(at_id, at_orientation, dir_)
        hash_ = tile_edges[at_id][(*at_orientation, dir_)]
        match = False
        for match_id, match_edge in tile_matches[hash_]:
            *match_orientation, match_dir = match_edge
            if match_dir == (dir_ + 2) % 4:
                print('|', match_id, match_orientation, match_dir)
                if match_id not in visited:
                    at_id = match_id
                    at_orientation = tuple(match_orientation)
                    visited.add(at_id)
                    match = True
                    print('|', 'matched')

        if not match:
            dir_i += 1
            if dir_i >= 2:
                corners.append(at_id)

    print('corners: {}'.format(corners))
    p1 = 1
    for c in corners:
        p1 *= c
    print('p1: {}'.format(p1))

    tile_width = int(math.sqrt(len(tiles)))

    at_id = corners[3]
    at_orientation = (0, False, False)
    visited = {at_id,}
    res = [[(at_id, *at_orientation)]]
    for i in range(tile_width):
        for j in range(tile_width):
            if i == 0 and j == 0:
                continue
            if j == 0:
                res.append([])
            if j != 0:
                prev_id, *prev_orientation = res[i][j - 1]
                dir_ = 1
            else:
                prev_id, *prev_orientation = res[i - 1][0]
                dir_ = 0

            print(i, j, dir_, prev_id, prev_orientation)
            hash_ = tile_edges[prev_id][(*prev_orientation, dir_)]
            match = False
            for match_id, match_edge in tile_matches[hash_]:
                *match_orientation, match_dir = match_edge
                if match_dir == (dir_ + 2) % 4:
                    print('|', match_id, match_edge)
                    if match_id not in visited:
                        res[i].append((match_id, *match_orientation))
                        visited.add(match_id)
                        match = True
                        break

            assert match

    res_ts = size - 2
    res_img = np.empty((tile_width * res_ts, tile_width * res_ts), dtype=np.uint8)
    for i in range(tile_width):
        for j in range(tile_width):
            id_, r_clockw, xflip, yflip = res[i][j]
            trans_tile = np.rot90(tiles[id_], k=r_clockw, axes=(1,0))
            if xflip:
                trans_tile = np.fliplr(trans_tile)
            if yflip:
                trans_tile = np.flipud(trans_tile)
            imi = tile_width - i - 1
            res_img[j * res_ts: (j+1) * res_ts, imi * res_ts: (imi+1) * res_ts] = \
                trans_tile[1:-1, 1:-1]

    res_len = tile_width * res_ts
    mon = np.array([
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0], 
        [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1], 
        [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]], dtype=np.uint8)
    for i in range(2):
        for xflip, yflip in itertools.product((False, True), repeat=2):
            trans_res = np.rot90(res_img, k=i, axes=(1,0))
            if xflip:
                trans_res = np.fliplr(trans_res)
            if yflip:
                trans_res = np.flipud(trans_res)

            mons = 0
            for y, x in itertools.product(range(res_len), repeat=2):
                if x + mon.shape[0] >= res_len or y + mon.shape[1] >= res_len:
                    continue

                trans_mon = trans_res[x: x+mon.shape[0], y: y+mon.shape[1]]
                assert trans_mon.shape == mon.shape
                if np.array_equal(trans_mon * mon, mon):
                    mons += 1

            if mons:
                p2 = np.sum(res_img) - (mons * np.sum(mon))
                print('p2: {} ({}, {}, {})'.format(p2, i, xflip, yflip))

if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    inp = parse_input(input_)
    #run(parse_input(read_input('input/day20_t0')))
    run(inp)
