import itertools
import math


class Moon:
    def __init__(self, id):
        self.id = id
        self.pos = 0
        self.vel = 0

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return '{}\tpos:{}\t\tvel:{}'.format(self.id, self.pos, self.vel)

    def apply_gravity(self, other):
        if self.pos > other.pos:
            self.vel -= 1
            other.vel += 1
        if self.pos < other.pos:
            self.vel += 1
            other.vel -= 1

    def apply_velocity(self):
        self.pos += self.vel


def state_hash(mns):
    return hash(tuple([(mn.pos, mn.vel) for mn in mns.values()]))


def solve_input():
    with open('input', 'r') as f:
        file_content = f.read().strip()
        solve(file_content)


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def sim_till(state_0, mns, i):
    while True:
        for m1, m2 in itertools.combinations(mns, 2):
            mns[m1].apply_gravity(mns[m2])

        for m in mns.values():
            m.apply_velocity()

        if state_0 == state_hash(mns):
            return i + 1

        i += 1


def solve(inp):
    moons = {0: {}, 1: {}, 2: {}}
    for i, line in enumerate(inp.split('\n')):
        pos = [int(x.strip()[2:]) for x in line[1:-1].split(',')]
        for j, p in enumerate(pos):
            moons[j][i] = Moon((j, i))
            moons[j][i].pos = p

    state_0 = [state_hash(moons[0]), state_hash(moons[1]), state_hash(moons[2])]
    i = {0: 0, 1: 0, 2: 0}
    for axis in i.keys():
        i[axis] = sim_till(state_0[axis], moons[axis], i[axis])

    print(i)
    print(lcm(lcm(i[0], i[1]), i[2]))


if __name__ == '__main__':
    # solve('<x=-1, y=0, z=2>\n<x=2, y=-10, z=-7>\n<x=4, y=-8, z=8>\n<x=3, y=5, z=-1>')
    # solve('<x=-8, y=-10, z=0>\n<x=5, y=5, z=10>\n<x=2, y=-7, z=3>\n<x=9, y=-8, z=-3>')
    solve_input()
