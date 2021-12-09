def solve_input(phases, repeat):
    with open('input', 'r') as f:
        file_content = f.read().strip()
        solve(file_content, phases, repeat)


def solve(inp, phases, repeat):
    signal = [int(x) for x in inp] * repeat
    offset = int(inp[:7])

    for i in range(phases):
        signal = phase(offset, signal)
        print('FFT at {}%'.format(i+1))

    if repeat == 1:
        print(''.join([str(x) for x in signal]))
    else:
        print(signal[offset: offset+8])


def phase(offset, signal):
    res = signal
    for i in range(offset, len(signal)):
        res[i] = sum(signal[i:])
        res[i] = abs(res[i]) % 10

    return res


if __name__ == '__main__':
    # solve('80871224585914546619083218645595', 100, 1)
    solve('03036732577212944063491565474664', 100, 10000)
    # solve_input(100)
