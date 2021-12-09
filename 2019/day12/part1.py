import itertools


class Moon:
    def __init__(self, id):
        self.id = id
        self.pos = [0, 0, 0]
        self.vel = [0, 0, 0]

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return '{}\tpos:{}\t\tvel:{}\t\tenergy:{}'.format(self.id, self.pos, self.vel, self.energy)

    def apply_gravity(self, other):
        for i in range(3):
            if self.pos[i] > other.pos[i]:
                self.vel[i] -= 1
                other.vel[i] += 1
            if self.pos[i] < other.pos[i]:
                self.vel[i] += 1
                other.vel[i] -= 1

    def apply_velocity(self):
        for i in range(3):
            self.pos[i] += self.vel[i]

    @property
    def pot(self):
        return sum([abs(x) for x in self.pos])

    @property
    def kin(self):
        return sum([abs(x) for x in self.vel])

    @property
    def energy(self):
        return self.pot * self.kin


def solve_input(steps):
    with open('input', 'r') as f:
        file_content = f.read().strip()
        solve(file_content, steps)


def solve(inp, steps):
    moons = []
    for i, line in enumerate(inp.split('\n')):
        pos = [int(x.strip()[2:]) for x in line[1:-1].split(',')]
        moons.append(Moon(i))
        moons[-1].pos = pos

    for _ in range(steps):
        for m1, m2 in itertools.combinations(moons, 2):
            m1.apply_gravity(m2)

        for m in moons:
            m.apply_velocity()

    for moon in moons:
        print(moon)
    print(sum([m.energy for m in moons]))


if __name__ == '__main__':
    # solve('<x=-1, y=0, z=2>\n<x=2, y=-10, z=-7>\n<x=4, y=-8, z=8>\n<x=3, y=5, z=-1>', 10)
    # solve('<x=-8, y=-10, z=0>\n<x=5, y=5, z=10>\n<x=2, y=-7, z=3>\n<x=9, y=-8, z=-3>', 100)
    solve_input(1000)
