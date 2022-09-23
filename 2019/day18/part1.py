from collections import OrderedDict


def solve_input(file):
    with open(file, 'r') as f:
        file_content = f.read().strip()
        solve(file_content)


def steps_req(MAP, y_1, x_1, y_2, x_2, keys=None):
    paths = [{'y_1': y_1, 'x_1': x_1, 'visited': [(y_1, x_1)], 'steps': 0}]
    accessible = ['.', '@']
    if keys is not None:
        for key in keys:
            accessible += [key, key.upper()]

    # Because searching uses BFS, visited can be global (first instance will always be shortest distance)
    visited = []
    while True:
        if len(paths) == 0:
            return None

        path = paths.pop(0)
        if path['y_1'] == y_2 and path['x_1'] == x_2:
            return path['steps']

        new_yx = [(path['y_1'], path['x_1'] + 1), (path['y_1'], path['x_1'] - 1),
                  (path['y_1'] + 1, path['x_1']), (path['y_1'] - 1, path['x_1'])]
        for new_y, new_x in new_yx:
            if new_y == y_2 and new_x == x_2:
                return path['steps'] + 1
            if MAP[new_y][new_x] in accessible and (new_y, new_x) not in visited:
                visited.append((new_y, new_x))
                paths.append({
                    'y_1': new_y,
                    'x_1': new_x,
                    'steps': path['steps'] + 1,
                })


def find(MAP, needle):
    for i, line in enumerate(MAP):
        if needle in line:
            return i, line.index(needle)


def find_keys_it(MAP, all_keys, Y, X):
    dist_hist = {}  # (frozenset((y_1, x_1), (y_2, x_2)), frozenset(keys)): dist

    key_paths = OrderedDict({(Y, X, frozenset()): 0})
    key_paths_hist = key_paths.copy()
    results = []
    i = 0
    while True:
        i += 1
        if len(key_paths) == 0:
            break

        print(len(key_paths), next(iter(key_paths.items())))

        kp_key, kp_steps = key_paths.popitem(last=False)
        if all_keys == kp_key[2]:
            results.append((kp_steps, kp_key[2]))
            continue

        access_keys = {}
        for key in (all_keys - kp_key[2]):
            key_y, key_x = find(MAP, key)
            dist_hist_key = (frozenset({(kp_key[0], kp_key[1]), (key_y, key_x)}), kp_key[2])
            if dist_hist_key in dist_hist and dist_hist[dist_hist_key] is not None:
                access_keys[key] = dist_hist[dist_hist_key]
            else:
                key_dist = steps_req(MAP, kp_key[0], kp_key[1], key_y, key_x, kp_key[2])
                dist_hist[dist_hist_key] = key_dist
                if key_dist is not None:
                    access_keys[key] = key_dist

        for key, dist in access_keys.items():
            new_kp_steps = kp_steps + dist
            new_pos = find(MAP, key)
            new_kp_key = (new_pos[0], new_pos[1], kp_key[2] | {key})

            if new_kp_key in key_paths_hist and key_paths_hist[new_kp_key] <= new_kp_steps:
                continue

            key_paths[new_kp_key] = new_kp_steps
            key_paths_hist[new_kp_key] = new_kp_steps

    return results


def solve(inp):
    all_keys = frozenset()
    MAP = []
    for line in inp.split('\n'):
        MAP.append([char for char in line])
        all_keys |= frozenset([char for char in line if char.islower() and char.isalpha()])

    Y, X = find(MAP, '@')

    print(min([d for d, _ in find_keys_it(MAP, all_keys, Y, X)]))


if __name__ == '__main__':
    # solve_input('input_t1')
    solve_input('input')
