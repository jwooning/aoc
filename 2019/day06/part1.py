import sys

nodes = {}


class Node:
    name = None
    children = None
    depth = None

    def __init__(self, n):
        self.name = n
        self.children = []
        self.depth = None

    def add_child(self, c):
        self.children.append(c)


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

    res = 0
    for _, n in nodes.items():
        res += n.depth

    return res


def set_tree_depths(node, d=0):
    node.depth = d
    for child in node.children:
        set_tree_depths(child, d + 1)


if __name__ == '__main__':
    # print(solve('COM)B\nB)C'))
    # print(solve('COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L'))
    print(solve_file(sys.argv[1]))

