import sys

import collections
import itertools
import functools

import numpy as np

seat = None

def read_input(path):
    with open(path, 'r') as f:
        return f.read().split('\n')

def parse_input(lines):
    return [l for l in lines if len(l)]

@functools.lru_cache()
def seat_neighbours(x, y):
    global seat

    res = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            xnew = max(0, min(x + i, seat.shape[0] - 1))
            ynew = max(0, min(y + j, seat.shape[1] - 1))
            res.add((xnew, ynew))

    res.remove((x, y))
    return res

@functools.lru_cache()
def seat_neighbours_ray(x, y):
    global seat

    res = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                try:
                    xnew = x
                    ynew = y
                    while True:
                        xnew += i
                        ynew += j
                        if seat[xnew][ynew] == 1:
                            break
                except IndexError:
                    pass

                if xnew >= 0 and ynew >= 0 and xnew < seat.shape[0] and ynew < seat.shape[1]:
                    res.append((xnew, ynew))

    return res

def run(inp):
    global seat

    seat = np.empty((len(inp[0]), len(inp)), dtype=np.uint8)
    occupied = np.empty((len(inp[0]), len(inp)), dtype=np.uint8)
    for j in range(0, len(inp)):
        for i in range(0, len(inp[0])):
            if inp[j][i] == '.':
                seat[i][j] = 0
                occupied[i][j] = 0
            elif inp[j][i] == 'L':
                seat[i][j] = 1
                occupied[i][j] = 0
            elif inp[j][i] == '#':
                seat[i][j] = 1
                occupied[i][j] = 1
            else:
                print('Invalid char {}'.format(inp[j][i]))

    print('p1: {}'.format(simulation(occupied.copy(), seat_neighbours, 4)))
    print('p2: {}'.format(simulation(occupied.copy(), seat_neighbours_ray, 5)))

def simulation(occupied, neigh_func, crowded):
    global seat

    change = True
    while True:
        if not change:
            break
        change = False

        new_occupied = occupied.copy()
        for i in range(0, occupied.shape[0]):
            for j in range(0, occupied.shape[1]):
                if seat[i][j] == 0:
                    continue

                if occupied[i][j] == 0 and sum(
                        [occupied[x][y] for x, y in neigh_func(i, j)]) == 0:
                    new_occupied[i][j] = 1
                    change = True
                elif occupied[i][j] == 1 and sum(
                        [occupied[x][y] for x, y in neigh_func(i, j)]) >= crowded:
                    new_occupied[i][j] = 0
                    change = True

        occupied = new_occupied

    return np.sum(occupied)


if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    inp = parse_input(input_)

    t0 = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""
    run(t0.split('\n'))
    run(inp)
