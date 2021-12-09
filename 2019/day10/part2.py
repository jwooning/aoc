import math
from collections import OrderedDict


def solve_input(x, y):
    with open('input', 'r') as f:
        file_content = f.read().strip()
        solve(file_content, x, y)


def solve(inp, x, y):
    ast_map = parse_ast_map(inp)
    for x_o, y_o in ast_map.keys():
        if x == x_o and y == y_o:  # Don't compare to self
            continue

        dx, dy = x_o - x, y_o - y
        angle = math.atan2(dx, -dy)
        if angle < 0:
            angle += 2 * math.pi
        if angle not in ast_map[(x, y)]:
            ast_map[(x, y)][angle] = []
        ast_map[(x, y)][angle] += [math.sqrt(dx**2 + dy**2)]
        ast_map[(x, y)][angle] = sorted(ast_map[(x, y)][angle])

    laser = OrderedDict(sorted(ast_map[(x, y)].items(), key=lambda z: z[0]))
    print(laser)
    i = 0
    while True:
        for a, asts in laser.items():
            if len(asts):
                ast = asts.pop(0)
                i += 1
                if i == 200:
                    print(x + (math.sin(a) * ast), y - (math.cos(a) * ast))
                    return


def parse_ast_map(inp):
    res = {}
    for y, line in enumerate(inp.split('\n')):
        for x, char in enumerate(line):
            if char == '#':
                res[(x, y)] = {}
    return res


if __name__ == '__main__':
    # solve('.#..##.###...#######\n' +
    #       '##.############..##.\n' +
    #       '.#.######.########.#\n' +
    #       '.###.#######.####.#.\n' +
    #       '#####.##.#.##.###.##\n' +
    #       '..#####..#.#########\n' +
    #       '####################\n' +
    #       '#.####....###.#.#.##\n' +
    #       '##.#################\n' +
    #       '#####.##.###..####..\n' +
    #       '..######..##.#######\n' +
    #       '####.##.####...##..#\n' +
    #       '.#####..#.######.###\n' +
    #       '##...#.##########...\n' +
    #       '#.##########.#######\n' +
    #       '.####.#.###.###.#.##\n' +
    #       '....##.##.###..#####\n' +
    #       '.#.#.###########.###\n' +
    #       '#.#.#.#####.####.###\n' +
    #       '###.##.####.##.#..##', 11, 13)

    solve_input(28, 29)

