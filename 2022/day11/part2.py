#!/usr/bin/env python

def solve_input():
  with open('input', 'r') as f:
    file_content = f.readlines()
    clean = [x.strip() for x in file_content]
    solve(clean)

def solve(inp):
  monks = []

  for i in range(len(inp)):
    if i % 7 == 0:
      monks.append({'p1': 0})
    elif i % 7 == 1:
      monks[-1]['i'] = eval('['+inp[i].split(':')[1]+']')
    elif i % 7 == 2:
      monks[-1]['o'] = inp[i].split(' = ')[1]
    elif i % 7 == 3:
      monks[-1]['t'] = int(inp[i].split(' ')[-1])
    elif i % 7 == 4:
      monks[-1]['tt'] = int(inp[i].split(' ')[-1])
    elif i % 7 == 5:
      monks[-1]['tf'] = int(inp[i].split(' ')[-1])

  cnm = 1
  for m in monks:
    cnm *= m['t']

  print(cnm)

  turn = 0
  for k in range(0, 10000 * len(monks)):
    while len(monks[turn]['i']) > 0:
      monks[turn]['p1'] += 1

      old = monks[turn]['i'].pop(0)
      item = eval(monks[turn]['o'])
      item = item % cnm

      to = monks[turn]['tt'] if item % monks[turn]['t'] == 0 else monks[turn]['tf']
      monks[to]['i'].append(item)

    turn = (turn + 1) % len(monks)

  most_active = sorted([x['p1'] for x in monks], reverse=True)
  p1 = most_active[0] * most_active[1]
  print(f'p1: {p1}')

if __name__ == '__main__':
  # solve(['Monkey 0:', 'Starting items: 79, 98', 'Operation: new = old * 19', 'Test: divisible by 23', 'If true: throw to monkey 2', 'If false: throw to monkey 3', '', 'Monkey 1:', 'Starting items: 54, 65, 75, 74', 'Operation: new = old + 6', 'Test: divisible by 19', 'If true: throw to monkey 2', 'If false: throw to monkey 0', '', 'Monkey 2:', 'Starting items: 79, 60, 97', 'Operation: new = old * old', 'Test: divisible by 13', 'If true: throw to monkey 1', 'If false: throw to monkey 3', '', 'Monkey 3:', 'Starting items: 74', 'Operation: new = old + 3', 'Test: divisible by 17', 'If true: throw to monkey 0', 'If false: throw to monkey 1'])
  solve_input()
