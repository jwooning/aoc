import sys

def solve(file_path):
    with open(file_path, 'r') as f:
        res = 0
        for line in f:
            w = int(line)
            res += calc_fuel_r(w)
        print(res)

def calc_fuel_r(weight):
    f = calc_fuel(weight)
    if f <= 0:
        return 0

    return f + calc_fuel_r(f)


def calc_fuel(weight):
    return (weight // 3) - 2


if __name__ == '__main__':
    solve(sys.argv[1])

