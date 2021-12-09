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

    ORE_PER_FUEL = 114125
    PROD_FUEL = 0
    ORE = 1000000000000
    REQS = {'FUEL': (ORE // ORE_PER_FUEL) * 1.373}
    LEFTOVER = {}
    while ORE > 0:
        if len(REQS):
            req_mat, req_quant = REQS.popitem()
        else:
            req_mat = 'FUEL'
            req_quant = 1

        if req_mat == 'FUEL':
            PROD_FUEL += req_quant

        mult = math.ceil(req_quant / REACTS[req_mat]['quant'])

        if REACTS[req_mat]['quant'] * mult > req_quant:
            if req_mat not in LEFTOVER:
                LEFTOVER[req_mat] = 0
            LEFTOVER[req_mat] += (REACTS[req_mat]['quant'] * mult) - req_quant

        for mat, quant in REACTS[req_mat]['reqs'].items():
            mul_quant = quant * mult
            if mat == 'ORE':
                ORE -= mul_quant
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

        print(ORE)

    print(PROD_FUEL)


if __name__ == '__main__':
    # solve('157 ORE => 5 NZVS\n165 ORE => 6 DCFZ\n44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL\n12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ\n179 ORE => 7 PSHF\n177 ORE => 5 HKGWZ\n7 DCFZ, 7 PSHF => 2 XJWVT\n165 ORE => 2 GPVTF\n3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT')

    solve_input()
