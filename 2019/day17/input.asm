0       1       ADD     $330, $331, $332
4       109     A_BP    3564
6       1102    MUL     1182, 1, $15
10      1101    ADD     0, 1449, $24
14      1002    MUL     $0, 1, $570
18      1006    JUMP_0  $570, 36
21      101     ADD     0, $571, $0
25      1001    ADD     $570, -1, $570
29      1001    ADD     $24, 1, $24
33      1106    JUMP_0  0, 18
36      1008    EQ      $571, 0, $571
40      1001    ADD     $15, 1, $15
44      1008    EQ      $15, 1449, $570
48      1006    JUMP_0  $570, 14
51      21102   MUL     58, 1, $BP[0]
55      1105    JUMP_1  1, 786
58      1006    JUMP_0  $332, 62
61      99      HALT

62      21101   ADD     333, 0, $BP[1]
66      21102   MUL     1, 73, $BP[0]
70      1106    JUMP_0  0, 579
73      1101    ADD     0, 0, $572
77      1102    MUL     1, 0, $573
81      3       INP     $574
83      101     ADD     1, $573, $573
87      1007    LE      $574, 65, $570
91      1005    JUMP_1  $570, 151
94      107     LE      67, $574, $570
98      1005    JUMP_1  $570, 151
101     1001    ADD     $574, -64, $574
105     1002    MUL     $574, -1, $574
109     1001    ADD     $572, 1, $572
113     1007    LE      $572, 11, $570
117     1006    JUMP_0  $570, 165
120     101     ADD     1182, $572, $127
124     1001    ADD     $574, 0, $0
128     3       INP     $574
130     101     ADD     1, $573, $573
134     1008    EQ      $574, 10, $570
138     1005    JUMP_1  $570, 189
141     1008    EQ      $574, 44, $570
145     1006    JUMP_0  $570, 158
148     1105    JUMP_1  1, 81
151     21102   MUL     340, 1, $BP[1]
155     1106    JUMP_0  0, 177
158     21102   MUL     477, 1, $BP[1]
162     1105    JUMP_1  1, 177
165     21101   ADD     0, 514, $BP[1]
169     21101   ADD     176, 0, $BP[0]
173     1106    JUMP_0  0, 579
176     99      HALT    
177     21102   MUL     1, 184, $BP[0]
181     1105    JUMP_1  1, 579
184     4       OUT     $574
186     104     OUT     10
188     99      HALT    
189     1007    LE      $573, 22, $570
193     1006    JUMP_0  $570, 165
196     102     MUL     1, $572, $1182
200     21102   MUL     375, 1, $BP[1]
204     21102   MUL     1, 211, $BP[0]
208     1106    JUMP_0  0, 579
211     21101   ADD     1182, 11, $BP[1]
215     21102   MUL     222, 1, $BP[0]
219     1105    JUMP_1  1, 979
222     21101   ADD     388, 0, $BP[1]
226     21101   ADD     233, 0, $BP[0]
230     1105    JUMP_1  1, 579
233     21101   ADD     1182, 22, $BP[1]
237     21102   MUL     1, 244, $BP[0]
241     1105    JUMP_1  1, 979
244     21102   MUL     1, 401, $BP[1]
248     21102   MUL     255, 1, $BP[0]
252     1105    JUMP_1  1, 579
255     21101   ADD     1182, 33, $BP[1]
259     21102   MUL     1, 266, $BP[0]
263     1106    JUMP_0  0, 979
266     21102   MUL     1, 414, $BP[1]
270     21102   MUL     1, 277, $BP[0]
274     1105    JUMP_1  1, 579
277     3       INP     $575
279     1008    EQ      $575, 89, $570
283     1008    EQ      $575, 121, $575
287     1       ADD     $575, $570, $575
291     3       INP     $574
293     1008    EQ      $574, 10, $570
297     1006    JUMP_0  $570, 291
300     104     OUT     10
302     21102   MUL     1, 1182, $BP[1]
306     21101   ADD     313, 0, $BP[0]
310     1105    JUMP_1  1, 622
313     1005    JUMP_1  $575, 327
316     1102    MUL     1, 1, $575
320     21102   MUL     1, 327, $BP[0]
324     1105    JUMP_1  1, 786
327     4       OUT     $438
329     99      HALT    
330                     0, 1, 1, 6, 77, 97, 105, 110, 58, 10, 33, 10, 69, 120, 112, 101
346                     99, 116, 101, 100, 32, 102, 117, 110, 99, 116, 105, 111, 110, 32, 110, 97
362                     109, 101, 32, 98, 117, 116, 32, 103, 111, 116, 58, 32, 0, 12, 70, 117
378                     110, 99, 116, 105, 111, 110, 32, 65, 58, 10, 12, 70, 117, 110, 99, 116
394                     105, 111, 110, 32, 66, 58, 10, 12, 70, 117, 110, 99, 116, 105, 111, 110
410                     32, 67, 58, 10, 23, 67, 111, 110, 116, 105, 110, 117, 111, 117, 115, 32
426                     118, 105, 100, 101, 111, 32, 102, 101, 101, 100, 63, 10, 0, 37, 10, 69
442                     120, 112, 101, 99, 116, 101, 100, 32, 82, 44, 32, 76, 44, 32, 111, 114
458                     32, 100, 105, 115, 116, 97, 110, 99, 101, 32, 98, 117, 116, 32, 103, 111
474                     116, 58, 32, 36, 10, 69, 120, 112, 101, 99, 116, 101, 100, 32, 99, 111
490                     109, 109, 97, 32, 111, 114, 32, 110, 101, 119, 108, 105, 110, 101, 32, 98
506                     117, 116, 32, 103, 111, 116, 58, 32, 43, 10, 68, 101, 102, 105, 110, 105
522                     116, 105, 111, 110, 115, 32, 109, 97, 121, 32, 98, 101, 32, 97, 116, 32
538                     109, 111, 115, 116, 32, 50, 48, 32, 99, 104, 97, 114, 97, 99, 116, 101
554                     114, 115, 33, 10, 94, 62, 118, 60, 0, 1, 0, -1, -1, 0, 1, 0
570                     0, 0, 0, 0, 0, 1, 36, 16, 0
579     109     A_BP    4
581     1202    MUL     $BP[-3], 1, $586
585     21001   ADD     $0, 0, $BP[-1]
589     22101   ADD     1, $BP[-3], $BP[-3]
593     21102   MUL     0, 1, $BP[-2]
597     2208    EQ      $BP[-2], $BP[-1], $570
601     1005    JUMP_1  $570, 617
604     2201    ADD     $BP[-3], $BP[-2], $609
608     4       OUT     $0
610     21201   ADD     $BP[-2], 1, $BP[-2]
614     1105    JUMP_1  1, 597
617     109     A_BP    -4
619     2105    JUMP_1  1, $BP[0]
622     109     A_BP    5
624     2102    MUL     1, $BP[-4], $629
628     21002   MUL     $0, 1, $BP[-2]
632     22101   ADD     1, $BP[-4], $BP[-4]
636     21101   ADD     0, 0, $BP[-3]
640     2208    EQ      $BP[-3], $BP[-2], $570
644     1005    JUMP_1  $570, 781
647     2201    ADD     $BP[-4], $BP[-3], $652
651     21001   ADD     $0, 0, $BP[-1]
655     1208    EQ      $BP[-1], -4, $570
659     1005    JUMP_1  $570, 709
662     1208    EQ      $BP[-1], -5, $570
666     1005    JUMP_1  $570, 734
669     1207    LE      $BP[-1], 0, $570
673     1005    JUMP_1  $570, 759
676     1206    JUMP_0  $BP[-1], 774
679     1001    ADD     $578, 562, $684
683     1       ADD     $0, $576, $576
687     1001    ADD     $578, 566, $692
691     1       ADD     $0, $577, $577
695     21102   MUL     1, 702, $BP[0]
699     1106    JUMP_0  0, 786
702     21201   ADD     $BP[-1], -1, $BP[-1]
706     1106    JUMP_0  0, 676
709     1001    ADD     $578, 1, $578
713     1008    EQ      $578, 4, $570
717     1006    JUMP_0  $570, 724
720     1001    ADD     $578, -4, $578
724     21102   MUL     731, 1, $BP[0]
728     1106    JUMP_0  0, 786
731     1106    JUMP_0  0, 774
734     1001    ADD     $578, -1, $578
738     1008    EQ      $578, -1, $570
742     1006    JUMP_0  $570, 749
745     1001    ADD     $578, 4, $578
749     21102   MUL     756, 1, $BP[0]
753     1106    JUMP_0  0, 786
756     1105    JUMP_1  1, 774
759     21202   MUL     $BP[-1], -11, $BP[1]
763     22101   ADD     1182, $BP[1], $BP[1]
767     21101   ADD     0, 774, $BP[0]
771     1105    JUMP_1  1, 622
774     21201   ADD     $BP[-3], 1, $BP[-3]
778     1106    JUMP_0  0, 640
781     109     A_BP    -5
783     2106    JUMP_0  0, $BP[0]
786     109     A_BP    7
788     1005    JUMP_1  $575, 802
791     20102   MUL     1, $576, $BP[-6]
795     20102   MUL     1, $577, $BP[-5]
799     1105    JUMP_1  1, 814
802     21101   ADD     0, 0, $BP[-1]
806     21101   ADD     0, 0, $BP[-5]
810     21101   ADD     0, 0, $BP[-6]
814     20208   EQ      $BP[-6], $576, $BP[-2]
818     208     EQ      $BP[-5], $577, $570
822     22002   MUL     $570, $BP[-2], $BP[-2]
826     21202   MUL     $BP[-5], 45, $BP[-3]
830     22201   ADD     $BP[-6], $BP[-3], $BP[-3]
834     22101   ADD     1449, $BP[-3], $BP[-3]
838     1201    ADD     $BP[-3], 0, $843
842     1005    JUMP_1  $0, 863
845     21202   MUL     $BP[-2], 42, $BP[-4]
849     22101   ADD     46, $BP[-4], $BP[-4]
853     1206    JUMP_0  $BP[-2], 924
856     21102   MUL     1, 1, $BP[-1]
860     1106    JUMP_0  0, 924
863     1205    JUMP_1  $BP[-2], 873
866     21101   ADD     0, 35, $BP[-4]
870     1106    JUMP_0  0, 924
873     1201    ADD     $BP[-3], 0, $878
877     1008    EQ      $0, 1, $570
881     1006    JUMP_0  $570, 916
884     1001    ADD     $374, 1, $374
888     2102    MUL     1, $BP[-3], $895
892     1102    MUL     2, 1, $0
896     2102    MUL     1, $BP[-3], $902
900     1001    ADD     $438, 0, $438
904     2202    MUL     $BP[-6], $BP[-5], $570
908     1       ADD     $570, $374, $570
912     1       ADD     $570, $438, $438
916     1001    ADD     $578, 558, $921
920     21002   MUL     $0, 1, $BP[-4]
924     1006    JUMP_0  $575, 959
927     204     OUT     $BP[-4]
929     22101   ADD     1, $BP[-6], $BP[-6]
933     1208    EQ      $BP[-6], 45, $570
937     1006    JUMP_0  $570, 814
940     104     OUT     10
942     22101   ADD     1, $BP[-5], $BP[-5]
946     1208    EQ      $BP[-5], 47, $570
950     1006    JUMP_0  $570, 810
953     104     OUT     10
955     1206    JUMP_0  $BP[-1], 974
958     99      HALT    
959     1206    JUMP_0  $BP[-1], 974
962     1101    ADD     0, 1, $575
966     21101   ADD     0, 973, $BP[0]
970     1105    JUMP_1  1, 786
973     99      HALT    
974     109     A_BP    -7
976     2106    JUMP_0  0, $BP[0]
979     109     A_BP    6
981     21102   MUL     1, 0, $BP[-4]
985     21101   ADD     0, 0, $BP[-3]
989     203     INP     $BP[-2]
991     22101   ADD     1, $BP[-3], $BP[-3]
995     21208   EQ      $BP[-2], 82, $BP[-1]
999     1205    JUMP_1  $BP[-1], 1030
1002    21208   EQ      $BP[-2], 76, $BP[-1]
1006    1205    JUMP_1  $BP[-1], 1037
1009    21207   LE      $BP[-2], 48, $BP[-1]
1013    1205    JUMP_1  $BP[-1], 1124
1016    22107   LE      57, $BP[-2], $BP[-1]
1020    1205    JUMP_1  $BP[-1], 1124
1023    21201   ADD     $BP[-2], -48, $BP[-2]
1027    1106    JUMP_0  0, 1041
1030    21101   ADD     0, -4, $BP[-2]
1034    1105    JUMP_1  1, 1041
1037    21102   MUL     -5, 1, $BP[-2]
1041    21201   ADD     $BP[-4], 1, $BP[-4]
1045    21207   LE      $BP[-4], 11, $BP[-1]
1049    1206    JUMP_0  $BP[-1], 1138
1052    2201    ADD     $BP[-5], $BP[-4], $1059
1056    1201    ADD     $BP[-2], 0, $0
1060    203     INP     $BP[-2]
1062    22101   ADD     1, $BP[-3], $BP[-3]
1066    21207   LE      $BP[-2], 48, $BP[-1]
1070    1205    JUMP_1  $BP[-1], 1107
1073    22107   LE      57, $BP[-2], $BP[-1]
1077    1205    JUMP_1  $BP[-1], 1107
1080    21201   ADD     $BP[-2], -48, $BP[-2]
1084    2201    ADD     $BP[-5], $BP[-4], $1090
1088    20102   MUL     10, $0, $BP[-1]
1092    22201   ADD     $BP[-2], $BP[-1], $BP[-2]
1096    2201    ADD     $BP[-5], $BP[-4], $1103
1100    2101    ADD     0, $BP[-2], $0
1104    1105    JUMP_1  1, 1060
1107    21208   EQ      $BP[-2], 10, $BP[-1]
1111    1205    JUMP_1  $BP[-1], 1162
1114    21208   EQ      $BP[-2], 44, $BP[-1]
1118    1206    JUMP_0  $BP[-1], 1131
1121    1106    JUMP_0  0, 989
1124    21102   MUL     1, 439, $BP[1]
1128    1105    JUMP_1  1, 1150
1131    21101   ADD     0, 477, $BP[1]
1135    1105    JUMP_1  1, 1150
1138    21102   MUL     1, 514, $BP[1]
1142    21101   ADD     1149, 0, $BP[0]
1146    1105    JUMP_1  1, 579
1149    99      HALT    
1150    21102   MUL     1157, 1, $BP[0]
1154    1106    JUMP_0  0, 579
1157    204     OUT     $BP[-2]
1159    104     OUT     10
1161    99      HALT    
1162    21207   LE      $BP[-3], 22, $BP[-1]
1166    1206    JUMP_0  $BP[-1], 1138
1169    2101    ADD     0, $BP[-5], $1176
1173    1201    ADD     $BP[-4], 0, $0
1177    109     A_BP    -6
1179    2105    JUMP_1  1, $BP[0]
1182                    36, 9, 36, 1, 7, 1, 36, 1, 7, 1, 36, 1, 7, 1, 24, 7
1198                    5, 1, 7, 1, 24, 1, 5, 1, 5, 1, 7, 1, 24, 1, 5, 1
1214                    1, 13, 24, 1, 5, 1, 1, 1, 3, 1, 32, 1, 5, 1, 1, 1
1230                    3, 7, 26, 1, 5, 1, 1, 1, 9, 1, 26, 1, 5, 1, 1, 1
1246                    9, 1, 26, 1, 5, 1, 1, 1, 9, 1, 26, 9, 9, 1, 32, 1
1262                    11, 1, 32, 1, 11, 1, 32, 1, 11, 1, 32, 7, 5, 1, 44, 1
1278                    44, 1, 44, 1, 36, 9, 36, 1, 22, 9, 13, 1, 22, 1, 7, 1
1294                    13, 1, 20, 13, 9, 7, 16, 1, 1, 1, 7, 1, 1, 1, 9, 1
1310                    1, 1, 3, 1, 10, 5, 1, 1, 1, 1, 7, 1, 1, 1, 9, 1
1326                    1, 1, 3, 1, 10, 1, 3, 1, 1, 1, 1, 1, 7, 1, 1, 1
1342                    9, 1, 1, 1, 3, 1, 6, 13, 7, 1, 1, 1, 3, 5, 1, 1
1358                    1, 5, 6, 1, 3, 1, 3, 1, 1, 1, 9, 1, 1, 1, 3, 1
1374                    3, 1, 1, 1, 12, 1, 3, 7, 9, 13, 12, 1, 7, 1, 13, 1
1390                    3, 1, 3, 1, 14, 1, 7, 1, 13, 9, 14, 1, 7, 1, 17, 1
1406                    18, 9, 17, 7, 44, 1, 44, 1, 44, 1, 42, 9, 38, 1, 5, 1
1422                    38, 1, 5, 1, 38, 1, 5, 1, 38, 1, 5, 1, 38, 1, 5, 1
1438                    38, 1, 5, 1, 38, 1, 5, 1, 38, 7, 6

