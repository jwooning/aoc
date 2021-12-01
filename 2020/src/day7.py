import sys

import collections


t0 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""


class Bag:
    def __init__(self, name):
        self.name = name
        self.contains = []
        self.contained_in = []
        self.size = None


def read_input(path):
    with open(path, 'r') as f:
        for line in f:
            yield line[:-1]


def run(lines):
    map_ = {}
    for line in lines:
        if not line:
            continue

        line = line.replace(' bags', '').replace(' bag', '')

        bag0, bags_o = line[:-1].split(' contain ')
        bags_o = [b for b in bags_o.split(', ')]

        for b in [bag0] + [b[2:] for b in bags_o]:
            if b not in map_:
                map_[b] = Bag(b)

        map_[bag0].contains = []
        for b in bags_o:
            if b != 'no other':
                map_[bag0].contains.append((int(b[0]), map_[b[2:]]))

        for b in bags_o:
            map_[b[2:]].contained_in.append(map_[bag0])

    bags = set()
    queue = collections.deque([map_['shiny gold']])
    while len(queue):
        finger = queue.popleft()
        bags.add(finger.name)
        for bag in finger.contained_in:
            if bag.name not in bags:
                queue.append(bag)

    print("p1: {}".format(len(bags) - 1))

    queue = collections.deque([map_['shiny gold']])
    while len(queue):
        f = queue.popleft()
        if f.size is not None:
            continue

        sum_ = 1
        for amount, bag in f.contains:
            if bag.size is None:
                sum_ = None
                queue.appendleft(bag)
            elif sum_ is not None:
                sum_ += amount * bag.size

        if sum_ is not None:
            f.size = sum_
        else:
            queue.append(f)


    print("p2: {}".format(map_['shiny gold'].size))


if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    run(input_)
