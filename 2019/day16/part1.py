def solve_input(phases):
    with open('input', 'r') as f:
        file_content = f.read().strip()
        solve(file_content, phases)


def solve(inp, phases):
    base = [0, 1, 0, -1]
    signal = [int(x) for x in inp]

    for _ in range(phases):
        signal = phase(signal, base)

    print(''.join([str(x) for x in signal]))


def phase(signal, base):
    res = []
    for i, _ in enumerate(signal, 1):
        pattern = sum([[b] * i for b in base], [])
        e = []
        p_i = 1
        for s in signal:
            e.append(s * pattern[p_i])
            p_i = (p_i + 1) % len(pattern)

        res.append(abs(sum(e)) % 10)

    return res


if __name__ == '__main__':
    # solve('80871224585914546619083218645595', 100)

    solve_input(100)
