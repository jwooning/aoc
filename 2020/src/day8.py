import sys

import collections


def read_input(path):
    with open(path, 'r') as f:
        for line in f:
            yield line[:-1]


def run(lines):
    prog = list(lines)

    print("p1 {}".format(run_prog(prog)))

    for i in range(0, len(prog)):
        prog_new = prog.copy()
        if prog_new[i][:3] == 'nop' and prog_new[i] != 'nop +0':
            prog_new[i] = prog_new[i].replace('nop', 'jmp')
        elif prog_new[i][:3] == 'jmp':
            prog_new[i] = prog_new[i].replace('jmp', 'nop')
        else:
            continue

        res = run_prog(prog_new)
        if res[0] == 0:
            print("p2: {}", res[1])
            return


def run_prog(prog):
    reg_ret = 0
    reg_a = 0
    reg_pc = 0
    prevs = list()
    while reg_pc < len(prog):
        if reg_pc in prevs:
            reg_ret = 1
            break
        prevs.append(reg_pc)

        instr = prog[reg_pc]
        if instr.startswith('nop '):
            reg_pc += 1
        elif instr.startswith('acc '):
            reg_a += int(instr[4:])
            reg_pc += 1
        elif instr.startswith('jmp '):
            reg_pc += int(instr[4:])
        else:
            print('Invalid op: {}'.format(instr))

    return reg_ret, reg_a



if __name__ == '__main__':
    input_ = read_input(sys.argv[0].replace('src', 'input').replace('.py', ''))
    run(input_)
