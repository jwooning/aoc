import math


def solve_input():
    with open('input', 'r') as f:
        file_content = f.read().strip()
        solve(file_content)


def solve(inp):
    ast_map = parse_ast_map(inp)
    for x, y in ast_map.keys():
        for x_o, y_o in ast_map.keys():
            if x == x_o and y == y_o:  # Don't compare to self
                continue

            dx, dy = x_o - x, y_o - y
            ast_map[(x, y)].add(math.atan2(dy, dx))

    counts = [(ast, len(s)) for ast, s in ast_map.items()]
    print(sorted(counts, key=lambda x: x[1], reverse=True)[0])


def parse_ast_map(inp):
    res = {}
    for y, line in enumerate(inp.split('\n')):
        for x, char in enumerate(line):
            if char == '#':
                res[(x, y)] = set()
    return res


if __name__ == '__main__':
    # solve('.#..#\n.....\n#####\n....#\n...##')
    # solve('......#.#.\n#..#.#....\n..#######.\n.#.#.###..\n.#..#.....\n..#....#.#\n#..#....#.\n.##.#..###\n##...#..#.\n.#....####')

    solve_input()

