import sys

crosses = []
edges0 = []


class Cross:
    x = None
    y = None

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def dist(self):
        return abs(self.x) + abs(self.y)


class Node:
    line = None
    edges = []
    x = None
    y = None

    def __init__(self, l, x, y):
        self.line = l
        self.edges = []
        self.x = x
        self.y = y

    def connect(self, n):
        global edges0
        e = Edge(self, n)
        self.edges.append(e)
        n.edges.append(e)

        if self.line == 0:
            edges0.append(e)
        else:
            for e0 in edges0:
                e.add_if_cross(e0)


class Edge:
    node1 = None
    node2 = None
    length = None

    def __init__(self, n1, n2):
        self.node1 = n1
        self.node2 = n2
        self.length = abs(n1.x - n2.x) + abs(n1.y - n2.y)

    def other(self, n):
        if self.node1 == n:
            return self.node2
        if self.node2 == n:
            return self.node1
        return None

    @property
    def is_horizontal(self):
        return self.node1.x != self.node2.x

    def add_if_cross(self, e2):
        global crosses
        if (self.is_horizontal and not e2.is_horizontal) and \
                (self.node1.x < e2.node1.x < self.node2.x or self.node1.x > e2.node1.x > self.node2.x) and \
                (e2.node1.y < self.node1.y < e2.node2.y or e2.node1.y > self.node1.y > e2.node2.y):
            crosses.append(Cross(e2.node1.x, self.node1.y))
        elif (not self.is_horizontal and e2.is_horizontal) and \
                (self.node1.y < e2.node1.y < self.node2.y or self.node1.y > e2.node1.y > self.node2.y) and \
                (e2.node1.x < self.node1.x < e2.node2.x or e2.node1.x > self.node1.x > e2.node2.x):
            crosses.append(Cross(self.node1.x, e2.node1.y))


def solve_file(file_path):
    with open(file_path, 'r') as f:
        file_content = f.read()
        solve(file_content)


def solve(inp):
    global crosses
    lines = [x.split(',') for x in inp.strip().split("\n")]
    roots = [Node(0, 0, 0), Node(1, 0, 0)]

    for i, line in enumerate(lines):
        node = roots[i]
        for instr in line:
            new_x = node.x
            new_y = node.y
            if instr[0] == 'R':
                new_x += int(instr[1:])
            if instr[0] == 'L':
                new_x -= int(instr[1:])
            if instr[0] == 'U':
                new_y += int(instr[1:])
            if instr[0] == 'D':
                new_y -= int(instr[1:])

            n = Node(i, new_x, new_y)
            node.connect(n)
            node = n

    for cross in crosses:
        print('x: {}, y: {}\tdist: {}'.format(cross.x, cross.y, cross.dist))


if __name__ == '__main__':
    # solve("R8,U5,L5,D3\nU7,R6,D4,L4")
    # solve("R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83")
    # solve("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7")
    solve_file(sys.argv[1])

