from collections import OrderedDict
import math


def solve_input():
    with open('input', 'r') as f:
        file_content = f.read().strip()
        solve(file_content)


def solve(inp):
    REACTS = {}
    for line in inp.split('\n'):
        reqs, prod = [x.strip() for x in line.split('=>')]
        prod_quant, prod_mat = prod.strip().split(' ')
        assert prod_mat not in REACTS
        REACTS[prod_mat] = {'quant': int(prod_quant), 'reqs': {}}
        for req in reqs.split(','):
            quant, mat = req.strip().split(' ')
            REACTS[prod_mat]['reqs'][mat] = int(quant)

    REQS = {'FUEL': 1}
    LEFTOVER = {}
    REQ_ORE = 0
    while len(REQS) > 0:
        req_mat, req_quant = REQS.popitem()
        mult = math.ceil(req_quant / REACTS[req_mat]['quant'])

        if REACTS[req_mat]['quant'] * mult > req_quant:
            if req_mat not in LEFTOVER:
                LEFTOVER[req_mat] = 0
            LEFTOVER[req_mat] += (REACTS[req_mat]['quant'] * mult) - req_quant

        for mat, quant in REACTS[req_mat]['reqs'].items():
            mul_quant = quant * mult
            if mat == 'ORE':
                REQ_ORE += mul_quant
                continue

            if mat in LEFTOVER:
                mul_quant -= LEFTOVER[mat]
                del LEFTOVER[mat]

            if mul_quant == 0:
                continue
            elif mul_quant < 0:
                if mat not in LEFTOVER:
                    LEFTOVER[mat] = 0
                LEFTOVER[mat] += -mul_quant
                continue

            if mat not in REQS:
                REQS[mat] = 0
            REQS[mat] += mul_quant

        print(REQS)

    print(REQ_ORE)


if __name__ == '__main__':
    # solve('10 ORE => 10 A\n1 ORE => 1 B\n7 A, 1 B => 1 C\n7 A, 1 C => 1 D\n7 A, 1 D => 1 E\n7 A, 1 E => 1 FUEL')
    # solve('9 ORE => 2 A\n8 ORE => 3 B\n7 ORE => 5 C\n3 A, 4 B => 1 AB\n5 B, 7 C => 1 BC\n4 C, 1 A => 1 CA\n2 AB, 3 BC, 4 CA => 1 FUEL')

    solve_input()
