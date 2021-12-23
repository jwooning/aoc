#!/usr/bin/env python
import os
import sys
import struct
import copy
import math
import time
import itertools
import collections

import numpy as np
from scipy.spatial.transform import Rotation as R

def read_input(path):
  with open(path, 'r') as f:
    for line in f:
      yield line[:-1]

def run(in_):
  lines = [x for x in in_ if x]
  scans = []
  for l in lines:
    if l.startswith('---'):
      scans.append([])
    else:
      scans[-1].append(np.array([int(x) for x in l.split(',')] + [1]))

  fixes = {0: np.eye(4, dtype=np.int64)}
  rotations = []
  for i in range(3):
    for min_ in [-1, 1]:
      target = np.array([0]*3)
      target[i] = min_
      up = np.array([0]*3)
      up[(i+1)%3] = 1
      for j in range(4):
        rot = R.from_euler(['x', 'y', 'z'][i], 90*j, degrees=True).as_matrix().astype(np.int64)
        rotations.append(look_at(target, rot @ up))

  lens = []
  for k, s in enumerate(scans):
    lens.append({})
    for i, j in itertools.combinations(range(len(s)), 2):
      l = round(np.linalg.norm(s[i] - s[j]), 8)
      assert l not in lens[k]
      lens[k][l] = (i, j)

  while len(fixes) < len(scans):
    new_fixes = fixes.copy()
    for i, mat in fixes.items():
      for j in [x for x in range(len(scans)) if x not in fixes]:
        comm = {}
        for l, pair in lens[i].items():
          if l in lens[j]:
            comm[l] = (pair, lens[j][l])

        if len(comm) >= 66:  # 12 pairwise combinations
          si = set()
          sj = set()
          for pi, pj in comm.values():
            si |= set(pi)
            sj |= set(pj)

          si = list(si)
          sj = list(sj)
          for ai in itertools.combinations(range(len(si)), 12):
            ssi = [x for k, x in enumerate(si) if k in ai]
            for aj in itertools.combinations(range(len(sj)), 12):
              ssj = [x for k, x in enumerate(sj) if k in aj]

              # print(len(comm), len(ssi), len(ssj))

              bi = [scans[i][x] for x in ssi]
              bj = [scans[j][x] for x in ssj]
              centi = np.mean(bi, axis=0)
              for rot in rotations:
                bjr = [rot @ x for x in bj]
                centj = np.mean(bjr, axis=0)
                dist = centi - centj
                #print(i, j, len(comm), dist, np.round(dist).astype(np.int64))
                if not np.allclose(dist, np.round(dist).astype(np.int64)) or \
                    dist[0] >= 2000 or dist[1] >= 2000 or dist[2] >= 2000:
                  continue
                print(i, j, len(comm), dist)

                trans = np.eye(4, dtype=np.int64)
                trans[:,3] = np.round(dist).astype(np.int64)
                trans[3,3] = 1
                mat = trans @ rot

                go = 0
                for bjt in [mat @ x for x in bj]:
                  for x in bi:
                    if np.allclose(x, bjt):
                      go += 1
                      break

                print(go)

                if go >= 12:
                  new_fixes[j] = fixes[i] @ mat
                  break

              if j in new_fixes:
                break

    fixes = new_fixes

    print(len(fixes), fixes.keys())

  print(fixes)
  res = set()
  for i, scs in enumerate(scans):
    bs = [fixes[i] @ s for s in scs]
    res |= set([tuple(x) for x in bs])
  print(len(res))

  p2 = 0
  for i, j in itertools.combinations(range(len(fixes)), 2):
    p2 = max(p2, np.sum(np.abs(fixes[i][:,3] - fixes[j][:,3])))
  print(f'p2: {p2}')



def look_at(camera_target, up_vector):
  vector2 = np.cross(up_vector, camera_target)
  vector2 = vector2 / np.linalg.norm(vector2)
  vector3 = np.cross(camera_target, vector2)
  return np.array([
    [vector2[0], vector3[0], camera_target[0], 0.0],
    [vector2[1], vector3[1], camera_target[1], 0.0],
    [vector2[2], vector3[2], camera_target[2], 0.0],
    [0.0, 0.0, 0.0, 1.0]
  ]).astype(np.int64)

if __name__ == '__main__':
  curr = sys.argv[0]
  input_ = read_input(os.path.join(os.path.dirname(curr), '..', 'input', curr.replace('.py', '')))
  # input_ = ['--- scanner 0 ---','404,-588,-901','528,-643,409','-838,591,734','390,-675,-793','-537,-823,-458','-485,-357,347','-345,-311,381','-661,-816,-575','-876,649,763','-618,-824,-621','553,345,-567','474,580,667','-447,-329,318','-584,868,-557','544,-627,-890','564,392,-477','455,729,728','-892,524,684','-689,845,-530','423,-701,434','7,-33,-71','630,319,-379','443,580,662','-789,900,-551','459,-707,401','--- scanner 1 ---','686,422,578','605,423,415','515,917,-361','-336,658,858','95,138,22','-476,619,847','-340,-569,-846','567,-361,727','-460,603,-452','669,-402,600','729,430,532','-500,-761,534','-322,571,750','-466,-666,-811','-429,-592,574','-355,545,-477','703,-491,-529','-328,-685,520','413,935,-424','-391,539,-444','586,-435,557','-364,-763,-893','807,-499,-711','755,-354,-619','553,889,-390','--- scanner 2 ---','649,640,665','682,-795,504','-784,533,-524','-644,584,-595','-588,-843,648','-30,6,44','-674,560,763','500,723,-460','609,671,-379','-555,-800,653','-675,-892,-343','697,-426,-610','578,704,681','493,664,-388','-671,-858,530','-667,343,800','571,-461,-707','-138,-166,112','-889,563,-600','646,-828,498','640,759,510','-630,509,768','-681,-892,-333','673,-379,-804','-742,-814,-386','577,-820,562','--- scanner 3 ---','-589,542,597','605,-692,669','-500,565,-823','-660,373,557','-458,-679,-417','-488,449,543','-626,468,-788','338,-750,-386','528,-832,-391','562,-778,733','-938,-730,414','543,643,-506','-524,371,-870','407,773,750','-104,29,83','378,-903,-323','-778,-728,485','426,699,580','-438,-605,-362','-469,-447,-387','509,732,623','647,635,-688','-868,-804,481','614,-800,639','595,780,-596','--- scanner 4 ---','727,592,562','-293,-554,779','441,611,-461','-714,465,-776','-743,427,-804','-660,-479,-426','832,-632,460','927,-485,-438','408,393,-506','466,436,-512','110,16,151','-258,-428,682','-393,719,612','-211,-452,876','808,-476,-593','-575,615,604','-485,667,467','-680,325,-822','-627,-443,-432','872,-547,-609','833,512,582','807,604,487','839,-516,451','891,-625,532','-652,-548,-490','30,-46,-14']
  run(input_)
