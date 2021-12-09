import sys


def solve_file(file_path):
    with open(file_path, 'r') as f:
        file_content = f.read()
        solve(file_content)


def solve(inp):
    min_num, max_num = [int(x) for x in inp.split('-')]
    res = 0
    for i in range(min_num, max_num + 1):
        if is_valid(i):
            res += 1

    print(res)


def is_valid(num):
    s_num = '{}'.format(num)
    return has_double(s_num) and is_increasing(s_num)


def has_double(s_num):
    for i in range(1, len(s_num)):
        if s_num[i] == s_num[i - 1]:
            return True

    return False


def is_increasing(s_num):
    for i in range(1, len(s_num)):
        if s_num[i - 1] > s_num[i]:
            return False

    return True


if __name__ == '__main__':
    solve_file(sys.argv[1])

