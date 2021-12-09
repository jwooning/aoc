import sys
import numpy as np


def solve_file(file_path, xy):
    with open(file_path, 'r') as f:
        file_content = f.read().strip()
        solve(file_content, xy)


def solve(inp, xy):
    img = parse_img(inp, xy)
    layer_min_zero = np.argmin(np.count_nonzero(np.array(img == 0), axis=(1, 2)))
    layer = img[layer_min_zero]

    print(np.count_nonzero(np.array(layer == 1)) * np.count_nonzero(np.array(layer == 2)))


def parse_img(inp, xy):
    inp = [int(x) for x in inp]
    assert len(inp) % (xy[0] * xy[1]) == 0
    shape = (len(inp) // (xy[0] * xy[1]), xy[1], xy[0])
    img = np.reshape(np.array(inp, dtype=np.int), shape)
    return img


if __name__ == '__main__':
    # solve('003456789012', [3, 2])

    solve_file(sys.argv[1], [25, 6])

