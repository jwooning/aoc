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
    player = -1
    decks = [[], []]
    for line in inp:
        if line.startswith('Player'):
            player += 1
        else:
            decks[player].append(int(line))

    t0 = time.time()
    print('p1: {}'.format(p1([d.copy() for d in decks])))
    t1 = time.time()
    print('p1 time: {}'.format(t1 - t0))

    print('p2: {}'.format(p2([d.copy() for d in decks])))
    t2 = time.time()
    print('p1 time: {}'.format(t2 - t1))

def p2(decks):
    winner, decks = p2_game(decks)
    print(winner, decks[winner])
    p2 = 0
    for i, c in enumerate(decks[winner]):
        l = len(decks[winner])
        p2 += (l - i) * c

    return p2

def p2_game(decks, nest=1):
    prev_rounds = set()
    cards = [None, None]
    rounds = 0
    while len(decks[0]) and len(decks[1]):
        rounds += 1
        #print('Round {} (Game {})'.format(rounds, nest))
        #for i in range(2):
        #    print('P{} deck: {}'.format(i + 1, decks[i]))

        this_round = hash(tuple([tuple(d) for d in decks]))
        if this_round in prev_rounds:
            return 0, decks
        prev_rounds.add(this_round)

        for i in range(0, 2):
            cards[i] = decks[i].pop(0)

        #for i in range(2):
        #    print('P{} card: {}'.format(i + 1, cards[i]))

        if cards[0] > len(decks[0]) or cards[1] > len(decks[1]):
            win = 0 if cards[0] > cards[1] else 1
        else:
            win, _ = p2_game([decks[i][:c] for i, c in enumerate(cards)], nest+1)

        decks[win].append(cards[win])
        decks[win].append(cards[1 - win])

        #print('Winner P{}'.format(win + 1))

    return (0 if len(decks[0]) else 1), decks

def p1(decks):
    c = [None, None]
    while len(decks[0]) and len(decks[1]):
        for i in range(0, 2):
            c[i] = decks[i].pop(0)

        assert c[0] != c[1]
        win = 0 if c[0] > c[1] else 1
        decks[win].append(c[win])
        decks[win].append(c[1 - win])

    winner = 0 if len(decks[0]) else 1
    p1 = 0
    for i, c in enumerate(decks[winner]):
        l = len(decks[winner])
        p1 += (l - i) * c

    return p1

if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    inp = parse_input(input_)
    run("""Player 1:
9
2
6
3
1
Player 2:
5
8
4
7
10""".split('\n'))
    run(inp)
