import sys
import math
import collections
import itertools
import functools
import struct

import numpy as np

def read_input(path):
    with open(path, 'r') as f:
        return f.read().split('\n')

def parse_input(lines):
    return [l.strip() for l in lines if len(l)]

def run(inp):
    res = {}
    all_ingr = set()
    counts = {}
    for line in inp:
        ingredients, allergens = line[:-1].split(' (contains ')
        ingredients = set(ingredients.split(' '))
        allergens = allergens.split(', ')

        for ingr in ingredients:
            if ingr not in counts:
                counts[ingr] = 0
            counts[ingr] += 1

        all_ingr |= ingredients
        for algn in allergens:
            if algn not in res:
                res[algn] = ingredients.copy()
            else:
                res[algn] &= ingredients

    in_one = set()
    for k, v in res.items():
        print(k, v)
        in_one |= v
    not_allergen = all_ingr - in_one
    p1 = sum([counts[n_algn] for n_algn in not_allergen])
    print('p1: {}'.format(p1))
    print('p2: Solve by hand')

if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    inp = parse_input(input_)
    run("""mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".split('\n'))
    run(inp)
