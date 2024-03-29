0       3       INP     $1033
2       1008    EQ      $1033, 1, $1032
6       1005    JUMP_1  $1032, 31
9       1008    EQ      $1033, 2, $1032
13      1005    JUMP_1  $1032, 58
16      1008    EQ      $1033, 3, $1032
20      1005    JUMP_1  $1032, 81
23      1008    EQ      $1033, 4, $1032
27      1005    JUMP_1  $1032, 104
30      99      HALT

move_north:
31      102     MUL     1, $1034, $1039
35      1002    MUL     $1036, 1, $1041
39      1001    ADD     $1035, -1, $1040
43      1008    EQ      $1038, 0, $1043
47      102     MUL     -1, $1043, $1032
51      1       ADD     $1037, $1032, $1042
55      1105    JUMP_1  1, 124

move_south:
58      102     MUL     1, $1034, $1039
62      101     ADD     0, $1036, $1041
66      1001    ADD     $1035, 1, $1040
70      1008    EQ      $1038, 0, $1043         # $43 = $38 == 0
74      1       ADD     $1037, $1038, $1042     # $42 = $37 + $38
78      1105    JUMP_1  1, 124

move_west:
81      1001    ADD     $1034, -1, $1039
85      1008    EQ      $1036, 0, $1041
89      101     ADD     0, $1035, $1040
93      1001    ADD     $1038, 0, $1043
97      101     ADD     0, $1037, $1042
101     1105    JUMP_1  1, 124

move_east:
104     1001    ADD     $1034, 1, $1039         # $39 = $34 + 1
108     1008    EQ      $1036, 0, $1041         # $41 = $36
112     101     ADD     0, $1035, $1040         # $40 = $35
116     101     ADD     0, $1038, $1043         # $43 = $38
120     101     ADD     0, $1037, $1042         # $42 = $37

check_new_pos:
124     1006    JUMP_0  $1039, 217              # hit_wall
127     1006    JUMP_0  $1040, 217              # hit_wall
130     1008    EQ      $1039, 40, $1032
134     1005    JUMP_1  $1032, 217              # hit_wall
137     1008    EQ      $1040, 40, $1032
141     1005    JUMP_1  $1032, 217              # hit_wall
144     1008    EQ      $1039, 5, $1032
148     1006    JUMP_0  $1032, 165
151     1008    EQ      $1040, 9, $1032
155     1006    JUMP_0  $1032, 165
158     1102    MUL     1, 2, $1044
162     1105    JUMP_1  1, 224

move:                                           # if $41 * $42 == 0:
165     2       MUL     $1041, $1043, $1032     #   goto 179;
169     1006    JUMP_0  $1032, 179              # else:
172     1102    MUL     1, 1, $1044             #   $44 = 1;
176     1105    JUMP_1  1, 224                  #   goto 224;


179     1       ADD     $1041, $1043, $1032
183     1006    JUMP_0  $1032, 217              # if $41 + $43 == 0: goto 217
186     1       ADD     $1042, $1043, $1032     # VAR = 39($42 + $43) + $39 < 363
190     1001    ADD     $1032, -1, $1032
194     1002    MUL     $1032, 39, $1032
198     1       ADD     $1032, $1039, $1032
202     101     ADD     -1, $1032, $1032
206     101     ADD     252, $1032, $211
210     1007    LE      $0, 73, $1044
214     1106    JUMP_0  0, 224

hit_wall:
217     1101    ADD     0, 0, $1044
221     1106    JUMP_0  0, 224

update_data_and_output:
224     1006    JUMP_0  $1044, 247
227     101     ADD     0, $1039, $1034
231     1002    MUL     $1040, 1, $1035
235     1002    MUL     $1041, 1, $1036
239     1002    MUL     $1043, 1, $1038
243     101     ADD     0, $1042, $1037
247     4       OUT     $1044
249     1105    JUMP_1  1, 0


1032    0       # val
1033    0       # input
1034    21      # pos_x
1035    21      # pos_y
1036    1       #
1037    10      #
1038    1       #
1039    0       # req_pos_x
1040    0       # req_pos_y
1041    0       #
1042    0       #
1043    0       #
1044    0       # output






252                     43, 57, 94, 36, 95, 30, 10, 40, 88, 72, 99, 97, 53, 21, 87, 48
268                     77, 40, 75, 69, 46, 98, 78, 22, 21, 38, 17, 12, 96, 34, 94, 81
284                     18, 49, 92, 1, 26, 67, 48, 15, 80, 51, 60, 92, 9, 77, 89, 64
300                     15, 85, 53, 94, 84, 99, 70, 7, 8, 69, 79, 79, 41, 62, 98, 22
316                     94, 92, 69, 97, 65, 96, 47, 99, 71, 4, 75, 10, 89, 85, 13, 89
332                     93, 93, 33, 46, 80, 61, 80, 75, 47, 99, 54, 63, 54, 57, 99, 80
348                     97, 77, 48, 33, 97, 95, 92, 20, 75, 3, 90, 84, 1, 50, 15, 94
364                     80, 95, 93, 70, 22, 3, 74, 69, 27, 99, 91, 66, 99, 1, 67, 12
380                     94, 31, 78, 83, 51, 97, 25, 4, 92, 85, 3, 96, 60, 5, 98, 69
396                     23, 95, 70, 92, 99, 1, 5, 84, 51, 87, 60, 67, 56, 98, 44, 80
412                     71, 81, 59, 58, 97, 82, 48, 87, 4, 76, 87, 45, 23, 75, 62, 89
428                     29, 37, 83, 22, 89, 81, 48, 64, 92, 30, 13, 90, 89, 83, 50, 49
444                     14, 89, 2, 34, 39, 84, 88, 21, 1, 81, 41, 74, 95, 89, 37, 82
460                     30, 87, 11, 93, 78, 67, 99, 8, 95, 84, 26, 93, 9, 95, 7, 18
476                     93, 94, 55, 96, 50, 92, 97, 43, 88, 53, 22, 91, 91, 35, 5, 79
492                     34, 66, 56, 24, 95, 49, 86, 72, 98, 52, 19, 81, 10, 90, 78, 12
508                     76, 8, 37, 87, 62, 80, 98, 52, 19, 40, 97, 83, 70, 18, 94, 77
524                     62, 87, 13, 35, 90, 35, 78, 68, 84, 89, 77, 13, 71, 19, 81, 54
540                     96, 88, 22, 40, 99, 24, 62, 85, 37, 95, 97, 89, 64, 30, 18, 98
556                     95, 9, 27, 76, 85, 49, 99, 31, 55, 71, 89, 95, 86, 94, 69, 24
572                     98, 32, 84, 99, 72, 82, 89, 61, 75, 30, 90, 74, 10, 71, 14, 80
588                     55, 68, 61, 99, 54, 84, 49, 17, 74, 83, 79, 38, 25, 90, 38, 99
604                     36, 89, 14, 38, 80, 71, 92, 10, 4, 65, 35, 78, 95, 40, 36, 78
620                     13, 39, 83, 76, 82, 64, 16, 96, 95, 31, 75, 95, 79, 2, 89, 38
636                     36, 87, 36, 76, 81, 38, 42, 92, 38, 7, 83, 87, 83, 87, 54, 96
652                     99, 78, 50, 43, 94, 96, 41, 87, 77, 8, 90, 78, 72, 79, 49, 82
668                     82, 56, 13, 94, 34, 90, 44, 82, 22, 60, 96, 48, 97, 2, 88, 87
684                     47, 92, 40, 91, 4, 58, 93, 29, 61, 83, 98, 99, 7, 8, 91, 30
700                     15, 88, 20, 90, 79, 10, 93, 31, 41, 95, 94, 56, 94, 95, 70, 93
716                     50, 94, 40, 37, 42, 84, 45, 35, 59, 27, 75, 80, 52, 90, 93, 15
732                     21, 92, 18, 52, 96, 83, 1, 90, 86, 12, 79, 21, 38, 98, 13, 74
748                     99, 40, 85, 41, 60, 94, 54, 44, 98, 83, 35, 57, 76, 66, 94, 94
764                     59, 82, 62, 77, 76, 22, 87, 39, 95, 98, 5, 90, 60, 88, 46, 91
780                     23, 58, 16, 83, 79, 7, 99, 11, 53, 76, 12, 88, 96, 88, 35, 58
796                     63, 81, 12, 26, 79, 89, 79, 26, 28, 23, 5, 90, 1, 76, 85, 55
812                     74, 44, 42, 88, 78, 36, 83, 61, 86, 92, 37, 62, 82, 80, 60, 46
828                     78, 32, 76, 20, 56, 77, 81, 9, 40, 45, 81, 85, 46, 7, 65, 96
844                     90, 19, 83, 16, 78, 66, 25, 24, 87, 80, 55, 93, 71, 84, 21, 86
860                     38, 79, 80, 94, 11, 42, 81, 89, 56, 18, 81, 33, 86, 72, 48, 86
876                     90, 59, 10, 92, 35, 77, 39, 94, 58, 97, 36, 5, 90, 96, 87, 40
892                     21, 22, 74, 80, 42, 32, 59, 60, 96, 25, 26, 95, 54, 90, 54, 15
908                     18, 98, 61, 91, 58, 84, 2, 19, 83, 36, 87, 60, 99, 63, 34, 79
924                     84, 92, 25, 74, 62, 6, 76, 84, 33, 80, 54, 91, 84, 3, 83, 95
940                     34, 22, 92, 88, 6, 88, 93, 17, 87, 59, 95, 17, 98, 65, 24, 20
956                     90, 95, 31, 74, 93, 30, 66, 80, 79, 72, 98, 7, 74, 34, 87, 77
972                     3, 24, 4, 82, 93, 42, 53, 90, 47, 82, 65, 65, 16, 75, 91, 79
988                     20, 93, 77, 54, 71, 81, 47, 82, 18, 78, 94, 92, 63, 75, 36, 87
1004                    34, 87, 31, 92, 29, 98, 22, 80, 95, 91, 17, 97, 35, 79, 87, 87
1020                    61, 93, 93, 99, 63, 95, 36, 90, 78, 77, 61, 83
