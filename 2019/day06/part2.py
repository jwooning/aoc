import sys

nodes = {}


class Node:
    name = None
    children = None
    parent = None
    depth = None

    def __init__(self, n):
        self.name = n
        self.children = []
        self.depth = None

    def __eq__(self, other):
        return self.name == other.name

    def add_child(self, c):
        self.children.append(c)
        c.parent = self


def solve_file(file_path):
    with open(file_path, 'r') as f:
        file_content = f.read()
        return solve(file_content)


def solve(inp):
    global nodes

    orbs = inp.strip().split('\n')
    for orb in orbs:
        A, B = orb.split(')')
        if A not in nodes:
            nodes[A] = Node(A)
        if B not in nodes:
            nodes[B] = Node(B)

        nodes[A].add_child(nodes[B])

    set_tree_depths(nodes['COM'])

    return find_dist(nodes['YOU'].parent, nodes['SAN'].parent)


def find_dist(n1, n2):
    steps = 0
    if n1.depth > n2.depth:
        n1, n2 = n2, n1

    while n1.depth < n2.depth:
        n2 = n2.parent
        steps += 1

    while n1 != n2:
        n1 = n1.parent
        n2 = n2.parent
        steps += 2

    return steps


def set_tree_depths(node, d=0):
    node.depth = d
    for child in node.children:
        set_tree_depths(child, d + 1)


if __name__ == '__main__':
    # print(solve('COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN'))
    print(solve_file(sys.argv[1]))

