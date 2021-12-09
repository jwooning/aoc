import sys

INSTR = {
    '01': {
        'LEN': 3,
        'NAME': 'ADD',
    },
    '02': {
        'LEN': 3,
        'NAME': 'MUL',
    },
    '03': {
        'LEN': 1,
        'NAME': 'INP',
    },
    '04': {
        'LEN': 1,
        'NAME': 'OUT',
    },
    '05': {
        'LEN': 2,
        'NAME': 'JUMP_1',
    },
    '06': {
        'LEN': 2,
        'NAME': 'JUMP_0',
    },
    '07': {
        'LEN': 3,
        'NAME': 'LE',
    },
    '08': {
        'LEN': 3,
        'NAME': 'EQ',
    },
    '09': {
        'LEN': 1,
        'NAME': 'A_BP',
    },
    '99': {
        'LEN': 0,
        'NAME': 'HALT',
    },
}


DATA_LINE_LEN = 16
DATA_RANGES = []


def parse_ranges(args):
    global DATA_RANGES
    for r in args:
        start, end = [float('Inf') if x == '' else int(x) for x in r.split('-')]
        DATA_RANGES.append((start, end-1))


def decompile_file(file):
    with open(file, 'r') as f:
        file_content = f.read().strip()
        decompile(file_content)


def in_data_range(i):
    global DATA_RANGES
    for s, e in DATA_RANGES:
        if s <= i <= e:
            return True
    return False


def decompile(inp):
    global DATA_LINE_LEN
    opcodes = [int(x) for x in inp.split(',')]
    i = 0
    res = ''
    while i < len(opcodes):
        str_op = '{:05}'.format(opcodes[i])
        param_modes = [int(x) for x in str_op[2::-1]]

        if str_op[3:] not in INSTR or in_data_range(i):
            res += '{:<24}{}'.format(i, opcodes[i])
            j = 1
            while j < DATA_LINE_LEN and i + 1 < len(opcodes) and \
                    ('{:02}'.format(opcodes[i + 1])[-2:] not in INSTR or in_data_range(i)):
                i += 1
                j += 1
                res += ', {}'.format(opcodes[i])
            res += '\n'
            i += 1
            continue

        instr = INSTR[str_op[3:]]

        out_str = '{:<8}'.format(i)
        out_str += '{:<8}'.format(opcodes[i])
        out_str += '{:<8}'.format(instr['NAME'])
        params_str = []
        for j in range(instr['LEN']):
            if i + 1 + j < len(opcodes):
                if param_modes[j] == 0:
                    params_str.append('$' + str(opcodes[i + 1 + j]))
                if param_modes[j] == 1:
                    params_str.append(str(opcodes[i + 1 + j]))
                if param_modes[j] == 2:
                    params_str.append('$BP[' + str(opcodes[i + 1 + j]) + ']')

        out_str += ', '.join(params_str)
        res += out_str + '\n'

        i += 1 + instr['LEN']

    print(res)


if __name__ == '__main__':
    parse_ranges(sys.argv[2:])
    decompile_file(sys.argv[1])
