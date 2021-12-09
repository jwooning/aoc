import numpy as np

np.set_printoptions(linewidth=120)


def solve_input(xy):
    with open('input', 'r') as f:
        file_content = f.read().strip()
        solve(file_content, xy)


def solve(inp, xy):
    img = parse_img(inp, xy)
    res = img[0]
    for i in range(1, img.shape[0]):
        res = merge_layers(res, img[i])

    print(res)


def merge_layers(top, back):
    top_trans = np.array(top == 2, dtype=np.int)
    top_opaque = np.subtract(np.ones(top.shape, dtype=np.int), top_trans)
    return np.array(top * top_opaque + back * top_trans)


def parse_img(inp, xy):
    inp = [int(x) for x in inp]
    assert len(inp) % (xy[0] * xy[1]) == 0
    shape = (len(inp) // (xy[0] * xy[1]), xy[1], xy[0])
    img = np.reshape(np.array(inp, dtype=np.int), shape)
    return img


if __name__ == '__main__':
    # solve('0222112222120000', [2, 2])

    solve_input([25, 6])

