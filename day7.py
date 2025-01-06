from tqdm import tqdm

puzzle_input = """26529145: 55 2 60 801 22
15644706: 5 7 8 1 7 9 3 6 621 3 9 6
7232028116: 96 8 358 21 1 2 3 693 3
6124901: 61 1 10 7 27 1 763 1
2835562501: 875 9 6 8 4 5 8 2 5 9 450
79002336: 4 1 47 2 1 2 9 57 2 4 14 1
155208: 7 7 77 759 448
165963832: 9 8 4 159 4 9 7 5 788
8557500: 40 2 33 5 815 28
36136845: 7 956 9 6 43
307389087: 8 900 1 51 837
22311: 1 91 5 1 1 1 6 9 8 4 8 3
2959728488: 739 93 4 8 4 90
29766245: 387 3 327 3 2 2 44 1
552680188966: 8 702 385 54 30 7 778
90671: 905 1 10 6 68
407425: 42 97 25
7738181186575: 17 5 979 7 9 90 8 657 2
5044072: 5 33 2 86 11
6036576: 5 60 662 7 32 9 6 624
3825: 286 1 9 130 9
79330356: 3 79 3 63 9 51 3 8
201260: 3 55 5 347 2
12218086684: 66 56 180 866 73 6 5
8251098305: 536 3 17 7 196 22 5 6 6
189602: 391 4 24 1 2
366257052812: 1 99 1 4 3 967 7 9 803 9
10731: 9 4 113 93 49
65130022: 186 349 74 331 7 997
758356437: 2 756 31 7 39 437
1008330: 63 9 7 2 332
54711: 7 3 37 2 6 49 1 93 5 5 4 9
1067624596: 48 15 1 73 169 8 9 7
17406732: 1 740 672 3 7
38824896: 592 6 6 44 248
12141387923623: 365 5 77 323 19 864 8
478369: 82 9 699 56 302
7924176: 1 6 4 1 28 3 2 3 4 7 8 204
1263: 7 29 3 47 5
1110095376: 946 646 170 227 8
48175785: 197 53 915 192 99 5 1
2858140: 1 2 85 81 37
25229272: 200 430 73 4 73
1511: 6 3 7 357 7 960
24869430: 5 452 40 50 19 430
18089890560230: 640 9 4 360 784 230
53008005: 4 2 31 9 9 7 708 3 9 1 5 1
110846216: 833 1 9 243 73 129
126613: 45 2 4 5 7 18
9120280: 69 61 131 5 710 657
36967506: 5 738 6 645 105 6
134099712: 7 4 8 6 6 766 8 29 6 8 9 8
85812897: 61 2 58 985 7
851357: 58 19 8 13 54
49211248: 800 12 1 2 5 1 861 6 82
120135: 63 1 615 685 3
171543911: 6 92 25 6 7 5 2 51 88 1 1
267709134: 530 65 4 2 777
74600836674: 31 8 8 3 1 3 7 89 8 8 5 78
3192651: 5 317 4 9 99
5336622: 3 9 45 383 93
160967: 7 9 2 977 64
2674460: 7 955 4 3 7 2 54 37
3313675: 9 9 112 5 244 3 51 7 7 1
882864: 8 94 72 3 6 5 46 6 36
8397881: 839 7 6 66 216
28589819160: 2 3 5 7 959 366 140
99047: 96 935 96 1 70
1264204265: 7 63 42 43 42 65
16399: 23 341 15 3 22
16470: 37 1 92 229 45 315
125049: 6 114 9 6 30 8 14 11 1
3554666: 52 272 68 81 89
91272464: 1 240 8 92 92
208098: 8 5 7 8 85 9 5 5 1 9 3 3
3198: 5 638 9
28124995: 351 54 2 24 8
472956001377: 19 844 7 6 8 8 7 76 9 5
2524: 8 5 4 28 5 19 2 473 586
859887: 14 3 312 6 14
614214762: 2 51 36 8 35 74 6 3 222
53741: 7 8 2 293 275 79 21
2394: 52 44 1 89 17
938: 5 40 59 674 5
1400080: 1 5 78 2 55 74 4
300018317892: 4 545 7 32 66 5 7 1 89
1212971816: 722 70 48 6 4 29 7
3538: 85 6 8 4 82
218438: 5 89 4 5 58 65
520607: 712 731 1 59 76
7186: 45 89 7 8 48 29 5
58397: 5 4 3 972 77
19406866: 970 2 1 4 2 67
215250: 5 1 70 3 205
733720: 3 48 2 3 402 1 5 8
5765: 7 10 3 7 841
3701539026: 3 7 37 153 902 6
734448: 119 5 4 9 49 9 6 80 7 1 8
410670: 9 47 3 793 2 2 2 4 6
13542787973784: 4 6 92 1 212 4 4 68 4 3 8
106554: 10 655 4
52880: 178 7 21 274 2
14484792: 37 1 1 3 71 2 423 872
4562468933: 14 510 639 8 935
180065450: 20 2 45 654 50
54972315: 9 3 4 23 946 26 2 6 4 9 5
123109957: 41 99 337 9 36 1 12 7
2098921562: 95 16 98 78 5 6 2 1 562
59713628279: 6 17 5 6 2 2 8 2 82 4 3 9
326931984: 509 593 28 860 9 327
83337298: 8 909 55 94 121
898206: 63 40 66 347 864
118000460: 14 609 173 5 2 8 44 5
523698: 58 685 22 4 681 1 8
211680: 81 6 811 26 5 32
1970487: 4 7 7 3 7 490
3047560880: 3 74 19 640 49 158
2064067023: 40 189 34 9 6 90 9 3 3 3
186403339: 2 7 6 5 9 2 70 793 1 761
8812611: 8 812 518 92 4
169360: 8 3 13 4 327 1 5 5 4 6 2 8
37968: 85 4 627 7 6 3 3 397 5 8
518: 22 3 6 2 4 9 353
309888096: 24 538 240 95
839712710: 87 957 703 8 1 2 7 12
323891: 39 7 2 7 70
3847410280: 765 2 9 419 2 5 2 7 7 1
9813767: 44 839 98 3 767
9363766302: 37 4 1 2 4 99 88 9 7 7 9 9
1203390384: 69 88 14 55 502 76 7 2
10498281: 128 89 33 1 7 18 69
75264400: 78 4 96 358 42
255895: 35 1 453 7 691 5 29
584066825: 426 25 646 687 4 2 25
206296821: 83 88 840 9 1 65 12 2 3
1622: 21 47 157 7 2 43 2
76809: 3 29 5 83 1 8 163
68812309: 641 226 2 475 9
47777926078: 1 74 1 5 53 64 607 8
1764123398: 69 37 691 380 17
937902: 11 3 2 8 697 189 6
127410330129: 80 132 2 831 159
2097341: 36 101 60 58
727338: 71 54 119 3 8
9981: 4 3 2 492 201 286
9204: 3 579 6 5 293 197
951: 226 8 8 8 701
5610797639: 3 7 4 15 7 9 6 656 1 982
17551634566: 548 83 16 82 3 13
864: 54 18 29 62 5 49
106633368088: 25 2 8 7 3 416 86 6 68
229340160: 79 9 42 960 8
47037514: 396 2 307 316 118
149956: 89 5 789 812 2
77235: 511 547 73 2
63972: 5 751 576 13 3 569
1765167: 6 7 42 445 722
40111940486: 3 6 951 9 34 410 4 1 87
66520440: 13 9 25 8 140 162
9833: 3 107 2 2 1 6 5 7 6 33 7
8056667: 65 9 9 9 7 4 6 8 681 3 47
519667906: 3 3 2 19 542 75 3 9 9 6 7
27297454: 5 8 5 886 6 23 6 5 811 6
223319012286: 3 97 409 918 91 1 6
343927: 3 1 1 3 1 5 2 14 2 316 6
736966: 1 325 3 5 16 445 46
5473335165: 5 70 60 4 33 379 1 1 4 3
3425425408: 9 3 85 802 688 64
12665: 8 96 42 3 85
171273640: 4 3 5 626 6 8 95 7 5 3 2
820429214: 84 7 951 37 665 32 94
240506: 515 6 5 5 2 40 90 4 5 9 8
9071904: 2 4 344 815 905
7472416588: 18 40 3 8 7 2 807 5 4 4 5
4325417: 1 6 27 54 15
10965190264: 6 261 455 752 7
17078393: 50 5 29 2 8 2 196 3 85 8
1120555: 97 8 722 2 8
1982: 5 78 30 556 802 511
700066: 46 894 17 915 8 35
44863331937: 5 5 423 633 31 937
119662: 1 19 6 77 94
26751357840: 2 78 98 34 2 385 6 5 3
981264: 8 855 957 6 1 4
7957943: 6 217 128 5 178
32274977613: 492 97 97 166 42
6509631: 84 86 97 795 9
335940: 3 78 2 1 41 60 3 174 20
234483735: 7 9 650 9 1 5 649 6 5 5
3788980: 8 8 1 59 988
1320481361: 2 731 5 2 10 15 9 7 4
635619158: 2 66 42 12 789 4
42733318: 312 4 9 550 93 39 1 1 4
106482: 9 4 815 47 1 54 5
63717: 1 2 53 56 61
14383320540: 336 85 4 4 43 59 6 732
1740: 3 13 7 62 12 5 5
1135521: 78 71 5 9 755
11743: 2 44 869 3 4 3 500 260
49311: 5 6 8 1 9 994 2 50 1 9 18
5190: 3 3 865
43170: 269 5 5 9 2 1 369 9 80 6
2996256384: 399 60 4 237 6 88
609080744: 8 443 9 2 8 7 9 9 1 66 2 4
12409: 1 46 260 183 6
240354406: 7 78 26 440 6
4489244: 81 600 55 960 2 282
93886: 6 7 8 939 9 94 9 57 2 1 5
48989484178: 7 989 93 6 4 6 6 63 13
476250: 94 5 26 254 3 5
1801980: 47 3 2 10 9 71
184429200: 15 86 5 989 9 2 8 5 475
10265642: 50 5 3 968 7 1
4237164: 5 5 6 1 501 9 4 5 67 8 6 6
100757913474: 997 10 99 6 7 9 134 7 7
206573903: 5 1 708 63 9 3 4 18 8
9419741: 7 9 117 23 153 6 8 2 62
3752084: 36 4 10 631 577 6
428749: 222 6 75 2 1 76 4 66 43
136740: 62 5 8 86 5
203446: 451 45 9 48 338 101
2223984599: 738 4 31 90 5 8 201 5 9
15392688: 847 8 9 7 685 1 6 6 7 9 8
23141: 117 32 6 4 673
1898874036: 929 1 82 249 38
65000754: 5 3 3 1 7 4 67 29 6 8 89
3500100: 499 70 71 25 4
460137: 33 3 461 3 816 722 7
28458000: 3 7 6 62 9 850
1331701: 58 28 164 5 21
23520611783: 6 45 9 9 9 35 611 782
145174683: 126 63 5 222 692
582: 8 30 48 2 6
31884368643: 3 542 707 3 5 1 8 41 6
1171287: 205 426 8 611 3
2721458282011: 2 4 147 1 36 39 23 857
504123874: 813 4 32 9 31 9 5 276
77992: 76 1 993
56963: 7 562 2 3 7 4
6864359: 608 78 35 8 59
363497: 95 9 699 5 17
13629024366: 767 4 6 296 366
263864: 874 1 8 3 838 69 8 695
5231768: 6 59 334 63 1 8
368702: 8 46 643 59
826: 304 3 4 69 437 9
775167627: 564 54 84 5 303
15858: 1 1 8 2 5 67 1 6 5 963 5 5
186256: 7 8 1 1 27 443 8 3 8 1 8 2
3371059175: 7 94 4 8 7 1 9 2 7 6 473 5
15665241: 7 3 551 1 42 2 60 3 47
7082478019: 3 51 6 708 475 1 8
856856018: 60 204 8 70 19
408587: 2 6 8 6 293 52 1 4 2 7 3 3
2089348: 6 137 65 9 349
2173319: 8 1 4 1 3 429 298 1 5
2188488: 154 74 8 19 24
1404874016783: 962 544 35 767 7 83
319360860: 6 1 8 5 2 8 6 1 692 7 804
11178688: 2 9 8 2 6 4 29 99 2 6 8 88
1120432: 6 4 8 2 4 39 4 7 111 2 8
2459646: 6 44 13 8 63 9 482
1096523: 9 9 57 13 3 54 516 7 2
7293: 2 35 4 2 6 17 2
130839233: 5 710 4 4 47 972 5 252
101427: 13 780 2 10 6 1
627856145: 9 1 6 1 1 8 8 1 63 9 379 8
2149452473937: 6 8 8 977 52 473 939
739563889: 7 395 6 388 6 3
106538411: 54 2 367 642 33 5 411
12268145042: 767 9 5 8 1 71 9 5 5 4 7 8
1192725: 2 10 2 43 4 1 48 8 285
14890875431: 744 5 2 824 1 51 431
876184299737: 12 864 18 42 997 38
4233119: 4 2 331 10 9
188667386341: 97 2 4 4 30 7 2 9 37 6 3 7
3877931: 6 924 7 8 2 46 1 8
44262541: 539 7 30 54 82 252
46008882: 53 1 142 6 885
413664: 34 6 99 372 8
1386329088: 67 665 345 631 3
626896116: 871 9 719 1 6
6163: 3 29 5 665 4
154237: 2 66 5 8 6 918 458 3 89
2124219648: 5 9 8 509 5 7 9 237 4 46
15507840: 889 36 32 28 8 492 2 2
2006499: 64 8 49 921 451
53877: 3 3 980 1 3 2 9 3 44 6 7 2
93615243396: 43 9 4 6 6 729 2 4 3 3 9 6
38993398: 55 7 14 3 3 61 5 15 77
6740052: 5 6 4 4 2 86 622 44 9 6 1
1473: 2 2 3 5 123
1979: 70 6 1 26
5146315: 638 32 80 1 1 7 96 43
86286070: 876 985 7 3
56142175: 926 47 577 7 5
4240913856587: 3 5 3 409 3 5 7 32 8 586
11852694: 592 634 2 8 6
135584548: 748 94 14 161 6
64199: 629 1 58 92 897 2 4
61951471: 186 460 8 724 239
1914205: 5 8 33 199 6
2381726: 6 4 7 69 371 3 6 3 1 991
11539965360: 705 1 290 84 671
322: 20 2 6 4 2
24059889: 529 3 26 9 8 7 9 301 8 7
209708: 4 3 5 1 8 73 1 12 2 1 8
194196: 8 5 4 1 81 1 1 161 3 7 3 3
11755591176: 278 989 4 3 4 509 1 7
2395680320: 9 37 6 62 140 318
1686: 95 7 711 18
91449969: 82 9 44 9 9 69
2083855883: 4 1 9 685 5 7 4 5 2 8 98 7
8256928: 332 810 4 4 90 356 8
60574670: 2 10 766 949 5
18430: 870 941 6 4 256 1
342297320: 69 39 24 4 530
59618: 66 696 77 1 944
620034420: 64 7 91 16 115 4 20
422851: 7 83 587 7 5 2 2 7 8 27
885580500: 78 59 4 57 7 48 5 644
96754: 8 8 638 3 6 3 7 136 8 2 2
22505: 55 477 51 60 5 7
32647335: 7 2 8 4 5 72 4 7 713 4 5 1
89754486: 456 1 228 81 81 5 4 6
139424899: 433 8 8 208 4 899
18027334: 18 7 7 1 7 4 7 4 3 150 34
76557222871: 8 598 7 9 2 7 28 5 2 7 8
24080: 8 1 5 5 56
3926290: 19 6 200 2 60 67 23
2170658500: 68 6 911 73 2 5 4 1 4 4 5
7273673: 854 658 65 74 953
8441: 1 175 32 199 6 5
528820009: 1 10 51 698 3 3 69 1 6
12613261: 10 524 29 7 83
998422640: 9 6 58 297 6 5 92 7 460
3101356032: 3 7 4 5 2 2 3 8 5 792 96
505607578: 5 5 81 418 86 4 2 79 98
131328466: 35 4 938 4 31 5 488 3 6
368587140269: 723 6 160 1 5 316 267
93928970343: 28 3 19 95 9 317 4 4 1
480765244841: 4 7 3 7 76 5 24 483 5 5
552: 1 3 3 532 13
47630: 90 65 29 8 598
9690555: 559 689 4 86 6 5 15
1975918: 44 332 8 5 8 711 7 7
2796: 560 3 501 474 48 3 90
228591900: 5 4 405 8 5 587 6 2 2 6 2
249330041: 9 422 6 379 39 596
2478888: 927 191 4 14 36
277704: 6 45 581 438 888
198263063: 97 4 491 2 5 6 711 1 47
1679733: 3 479 35 9 361
34776: 7 12 56 63 84 3
109577: 39 5 9 72 574 78
396574: 7 68 223 4 4 4
4944056: 8 6 56 33 54 9 1 36 4 13
193864868: 709 9 3 9 48 68
77048: 72 7 4 430 8
51542400: 8 3 505 896 5
39699287: 56 713 13 7 96
145829: 3 7 289 7 510 88 7 27 6
7607704084: 945 5 95 99 31 8 84
164395: 7 146 8 3 396
428304: 7 6 8 304 1
24302: 2 399 31 4
23006927: 89 5 517 4 30
49469949: 735 73 922 27 12
1084: 98 95 5 34 86
2380136: 7 6 471 8 6 38 6 2 5 2 1 2
71661629: 5 18 88 721 30
636471896382: 8 7 4 86 8 8 3 9 866 382
238928323: 66 362 8 315 8
10458541: 90 242 1 7 5 1 8 2 8 6 1
379085972028: 7 2 282 812 2 8 6 9 12
14183252062: 3 93 979 21 2 6 6 1 36
713463: 44 2 802 6 4 2 9 6 968
167038768623: 52 5 998 8 6 8 6 16 3 3
29203: 5 584 3 1
170394818: 1 253 909 738 950
65861220831339: 67 983 220 831 339
6388077995: 5 4 754 82 9 93 996
4389657286: 9 7 5 605 6 4 938 91 7 7
812896: 87 2 7 2 8 7 5 14 3 4 7 4
593252: 7 5 4 6 4 659 1 8 8 1 9 8
14747959296: 51 6 6 64 188 512 7
124617990420: 929 64 20 690 67 421
1156: 8 277 6 94 3
39415082: 6 3 7 28 7 3 4 7 1 40 243
833: 1 3 6 35 1 3 2 8 409 8 52
28876: 3 354 770 7 8
59200: 13 5 2 530 74
7239223518: 147 9 3 2 699 7 300 1 5
14790302635: 4 9 1 30 10 5 1 4 3 8 6 7
2219575: 97 286 80 209 6
541388: 6 8 606 873 15 73 40
83635717: 75 242 18 256 517
6702372884: 9 45 4 7 7 6 97 7 2 3 5 81
12177895: 99 123 8 9 5
997751136: 7 229 1 69 8 2 4 4 909 4
1565222: 2 78 522 2
143: 6 8 9 82 4
2410: 73 3 425 2 92 2
76285: 6 6 2 683 73
305618823174: 6 366 99 6 82 6 1 6 8 6 6
114679: 7 2 2 332 75 2 8 26 3 66
21747186: 7 5 425 991 8 6 3 2 32 9
55159211524: 2 568 6 9 6 2 7 7 8 4 8 4
908: 8 24 1 78 5
138231486043: 67 859 378 3 3 706 7
2046600: 9 6 78 6 2 40 7 8 5 7 6 5
179020160: 31 655 463 862 10
2915703: 93 354 591 87 72
145656: 5 215 948 8 1 9
24803997: 7 612 7 4 4 621 3 7 1 4 3
2912075: 1 2 74 4 98 8 208 7 71 4
2089670340: 949 60 25 22 340
1704348464: 4 194 18 86 463
142857: 4 6 9 381 6 87 1 69 9 3
8664: 14 1 87 861 4
84848431615025: 897 8 67 6 7 9 46 5 5 25
880290: 83 28 6 7 9 99 81 7 3 3 9
33282652: 8 8 64 1 2 490 153 9
184248: 48 3 4 72 9
5559216: 5 55 9 2 15
27240682959: 8 294 674 2 55 1 1 1 9
855: 2 3 741 29 79
19162077441: 674 41 268 774 41
101583528: 505 386 67 3 941
12096608: 9 1 73 78 9 83 6 2 3 186
105651: 11 36 412 30 7 6 3 4 59
96730445: 3 9 5 2 7 185 7 9 9 4 9 5
179072560: 38 927 46 5 78 41 19
346056: 5 37 3 3 2 2 7 5 64 7 200
1424111870: 592 1 3 799 1 3 2 8 70
1022258: 4 4 12 494 258
145862: 3 9 6 9 62
8809062: 8 9 8 2 3 2 1 291 1 97 1 5
799374577: 197 7 97 18 4 83 83
15799745304: 69 8 553 639 81
130326925: 344 57 6 7 4 89 69 28 1
21139445: 21 1 17 22 442
414390080: 3 55 5 6 5 4 71 32 598
53601647492: 7 5 55 7 229 6 651 92
14071632960: 7 6 5 32 76 1 9 672 41
2314710: 9 48 8 846 4 5 6
810396: 4 6 12 81 8 151
3984441307: 3 9 844 41 242 8 8 50 2
6355972: 7 943 2 893 95 1
655261982: 4 4 2 9 5 3 8 613 420 6 2
13366: 84 16 794 6 12 526
492: 481 8 1 2
13112208958: 52 1 76 3 5 3 9 276 958
2093304: 7 48 50 761 72 482
16544895: 9 8 469 6 4 66 1 2 28 87
663542713: 1 5 49 2 8 5 62 7 9 852 1
7003042: 17 22 6 4 88 1 7 22 41
36805266: 6 12 1 4 6 25 7 990 8 9
23875: 4 1 213 110 3
958057102630: 957 387 670 102 6 30
570649268: 8 2 2 5 3 68 60 6 4 9 267
287148863376: 7 976 357 315 1 36
36806622: 956 55 8 9 7
11262783: 727 154 70 586 5 8 81
25406: 5 8 728 33 3 57 2
73018446203: 7 5 5 7 7 90 8 718 3 4 5 4
7349620: 73 49 5 41 82
493547673654: 725 3 1 1 36 9 6 6 87 7 6
57749310137: 1 691 30 86 6 368 8 7 8
203320: 69 64 1 3 46
2558784: 10 66 3 48 8
408577094: 8 608 6 8 5 7 5 4 5 527 2
238184: 3 1 74 954 524 3 9 19 8
152919: 5 52 84 45 393 1 6 35
5373046: 57 24 80 214 49
474110270: 4 738 3 10 263 9
93569: 7 4 4 835 6 6 20 1 13 1 4
15: 8 2 5
416450: 35 6 6 451 2
91075: 4 1 1 18 5 89 96 2 7 2 59
937: 1 427 40 467 2
9088256711: 93 18 19 882 6 3 9 11
1871434: 1 4 92 65 396 9 1 8 326
11500132: 7 4 4 7 27 3 9 147 620 1
4824485: 2 4 2 5 7 3 95 6 2 445 3 6
6459840: 3 6 4 12 5 26 38 2 3 72 8
23528076490: 1 56 6 4 680 75 5 6 93 1
87847240401: 7 650 7 147 9 40 399 5
263846: 6 7 1 2 1 846
5388: 4 527 132 2 2 904
11405: 5 3 105 79 26
164275: 3 38 486 7
1120392: 38 8 9 4 25 96 3 9
36685: 5 7 1 672 13
1251: 1 3 8 46 5 16 91 35
4038724: 71 7 26 6 3 7 77
1000058599: 188 6 41 73 1 171 1 9 5
470299536: 7 56 1 2 546 62 9 1 92 6
642188: 16 2 237 2 349 724
1745832: 436 4 5 8 4
3885769: 5 3 113 1 6 310 461
61166948800: 5 53 958 338 974 2 50
430580268: 1 19 6 6 8 9 6 6 9 596 6 8
947520: 1 3 1 23 4 7 12 7 6 96 42
6626636: 846 97 68 7 655
1825: 344 258 690 50 483
16748119: 8 373 58 5 97 2 748 7
883750: 992 3 7 8 875
82833817075: 346 2 9 522 92 26 452
79114: 6 77 9 44 16
8605090378528: 223 50 8 8 410 55 4 7
6927529562: 16 99 10 64 331 23 94
56535358: 6 78 74 31 905 5
10307183: 6 4 307 1 8 3
11123091647: 5 78 321 741 1 96 622
8089248: 66 79 2 4 362 38 8 712
264728: 5 822 320 19 5 3 63
3353415: 48 519 789 68 471
39796323: 7 954 6 5 41 64 5
11895360069: 148 692 800 6 9
886357962195: 5 7 3 7 378 147 7 1 193
377447760: 8 504 6 26 1 6 860 60
422234688: 2 3 931 5 7 3 41 6 8 8 8 1
17830537: 8 9 5 2 1 4 1 7 6 3 5 537
218: 66 10 75 53 14
104016: 8 95 46 4 551
112030: 1 20 949 484 219 67 6
10348: 21 80 4 6 244
125224704: 3 11 9 4 11 348 8 8 9 99
727: 37 5 73 23 446
1076408: 904 2 3 119 51
216161: 1 4 15 9 1 6 796 3 361
48703715: 7 2 54 63 40 7 1 6
3505644464: 418 8 820 7 3 4 8 2 464
117341: 4 1 280 4 2 4 8 4 9 6 1 5
5405988: 4 9 1 462 38 5 22 9
2707476024: 714 75 4 66 766
1739996: 8 1 72 867 999
530877018: 853 7 62 889
24337135: 991 3 9 36 3 7 908 2 1 8
118448712: 1 22 13 45 64 9 8
1243: 8 5 79 1 2 1 3 6 2 498 4 3
437901: 13 8 566 2 373
1085420: 31 70 5 3 4 5
885174185587: 619 286 83 7 117 5
10487968134: 253 423 758 325 98
183627752: 18 3 62 7 174 576
2574965810: 26 302 979 12
56483847: 4 6 6 5 1 3 2 987 5 69 63
612445154: 7 4 8 3 7 1 81 6 35 54
840482: 81 93 69 6 7 23
18183842: 190 957 43 5 794
53314: 52 8 136 96 322
202324794: 7 2 281 439 32 9 76
166183: 5 3 7 72 4 18 4 879 2 9 3
5753: 57 47 5
75335933: 9 3 3 9 30 5 933
83496: 9 7 9 494 8
6739975: 6 8 9 2 8 3 196 98 9 1 5 5
5049947640429: 86 665 80 883 429
3073243026: 7 439 2 430 26
259372157: 6 4 3 5 9 37 670 4 5 8 4 4
258395: 31 2 91 7 64 24
21236041625400: 63 42 7 75 876 831 3 7
3929856897: 860 816 56 81 9 7 802
17405956064: 696 5 1 5 9 559 5 6 5 6
157075: 89 28 3 93 92 515
36027252854361: 584 858 616 543 59
34360: 21 163 1 9 31 80
35295647590: 182 87 9 193 591
91658: 916 5 8
1285629: 774 308 506 809 937
8557158: 26 4 408 2 699
3216398: 91 147 56 773 6 228 2
13979270: 411 68 2 7 5 5 6 9 56 2 8
2520: 5 7 1 9 7
177154248: 82 3 8 241 62 9 9 688 8
3045871709: 9 77 1 72 682 2 8 515
21900712: 857 7 84 5 6 1 2 1 1 7 1 3
9423: 55 957 28 7 9
36662: 847 76 3 13 1 664
309457: 12 8 5 3 9 370 88
2414291: 34 71 290
131138: 37 14 253 87
1812720: 5 90 6 73 178 3 6 80
148520: 9 1 270 69 10 9 6 572
3896881933: 3 6 5 169 6 3 87 4 7 933
2191252980: 9 30 443 2 673 8 961 7
22257277935: 44 3 35 36 5 2 399 466
6069489: 1 19 22 703 8 10 442 3
3975: 9 238 68 7 818
10644718092: 4 8 7 144 4 7 7 8 6 42 2 6
4634: 459 4 6
8884765292: 2 9 60 7 8 874 3 7 30 3
109342080: 11 4 448 9 82 8 8 5
194683: 64 1 3 19 4 8 3
766211: 2 893 13 33 19
148357436: 85 3 8 68 727
20586507: 58 69 34 57 51
23062903: 3 512 4 18 30 74 2 63
27156: 3 83 7 73 4
151543657440: 2 739 88 467 20 261 7
740: 70 3 28 501 1
1973769124: 8 614 53 349 432 6 1
9065175: 95 3 11 8 66 58 9 453 9
24041351: 5 48 413 51
10041339: 920 84 13 37
3489183: 5 8 64 595 5 7 91
1169: 596 196 343 34
37289: 32 6 9 30 89
284855: 213 6 11 13 5 8
4050777: 64 779 91 6 8 8
1694: 173 657 8 9 2
3551433: 2 1 503 816 107 10 3
376327448: 8 84 56 663 80 1 2 4 2
58554: 38 78 5 3 385
656898: 264 5 285 9 407
182009103: 62 2 46 35 77 618 687
1010491949: 3 5 6 145 9 108 719
177030: 310 77 832 1 588 7
89939900: 8 985 1 80 8 900
42338464: 5 9 5 9 7 92 1 38 7 36 9 7
355821209: 468 95 14 3 65 8 4 8
778738: 39 9 8 4 2 3 2 217 9 1 5
17925613: 7 29 883 70 643
8826920: 88 26 9 1 8
516531662: 997 21 8 507 1 64
104515118: 8 72 1 320 6 4 9 63 8
76360883785: 98 646 6 549 6 1 235
8863350398: 5 473 5 5 5 185 1 6 2 8 1
117551442: 5 256 2 7 7 446 87 589
568480392: 710 5 999 16 5 472
112215975: 3 37 47 74 31 21 7 75
343116: 3 5 577 9 4
1857618222: 202 4 8 886 207 223
1016293275: 99 8 94 3 83 6 22 12 6
1799952: 5 2 66 974 4
7571815783: 75 71 81 5 785
26883081: 2 6 88 217 34 2 6 563
25536148: 2 3 5 532 8 2 6 2 8 5 3 5
20094714884: 5 61 158 9 15 3 439
3949: 723 21 1 3 714 998 1 2
24465516: 4 82 5 4 2 8 1 8 8 42 597
411974054: 4 369 60 518 57 8 9 95
336476724: 5 21 937 570 4 6
391121107426: 46 4 386 263 27 7 46 7
2167452523206: 4 9 379 3 36 2 3 6 2 6 9 9
48492089: 50 124 1 49 5 9 24 89
30118331: 9 3 13 8 7 3 7 1 183 28 3
8919388: 8 871 29 6 1 84 48 87
42678923: 42 67 82 2 68 5 452
1191546920: 8 4 2 74 8 5 9 5 92 920 2
249685: 157 92 685
529545744: 61 89 1 2 593 7 546 23
28860892: 69 519 265 8 90
1541: 36 8 9 42 202 19 882
226288255: 754 20 61 874 30 207
613983155: 79 6 1 2 711 872 7 7
27666056: 536 58 23 7 506 4
49867020: 2 2 396 92 82 342
2328480: 5 71 1 630 48
83896869770: 4 1 72 7 7 9 7 2 2 9 5 322
1224946936318: 8 598 94 894 3 32 5 16
354929: 20 467 38 1 9
12674536: 128 466 2 98 217
5384: 1 9 539 436 8 89
668: 6 11 9
59145841716: 9 8 7 81 6 923 1 707 8
956305971: 5 1 68 38 90 801 81
104508247032: 6 2 968 7 4 1 7 3 7 36 6 7
699: 8 4 4 5 8 3 44 31 3 25 2 7
1015882165: 3 5 76 3 4 6 8 3 6 3 5 99
914753556: 8 38 9 165 6 1 7 5 3 1 4
750592: 462 1 9 2 9 5 5 2 7 29 2
25989: 620 6 3 4 80 2 9
178077: 1 7 800 1 76
1783769832: 6 5 9 2 8 7 4 9 87 5 2 936
525226: 96 1 3 6 9 7 1 94 7 2
590376: 12 1 6 10 244 9 1 2 3 68
9902675: 990 2 1 352 321
1561076: 136 2 3 19 296 3 6 2 3
2754000: 7 1 94 81 6 5 300
5094760: 7 5 9 5 84 7 5 12 72 77 8
1428213: 5 3 86 9 9 4
3294883: 58 1 28 6 8 789 16
2990738514: 6 43 483 1 6 6 2 1 1 7 4 6
116126: 390 3 500 1 3 13
676588258: 65 8 155 6 892 67 2 9
3515286: 1 2 508 7 286
30397272484841: 9 95 611 449 5 5 9 843
1142424: 7 466 6 1 2 4 2 714 5
358188478: 9 3 569 3 60 6 6 3 8 3 5 6
919: 8 97 9 4 6
9509449393: 88 2 29 68 186 29
4007898: 6 46 561 9 7 9 3 1 8 650
2053908: 5 2 18 3 4 1 2 6 3 21 77 9
1849044293: 12 8 4 3 8 6 8 34 2 4 83 2
3760861: 260 3 3 8 5 36 30 2 2
80722435248: 159 258 371 442 6 2
228864929: 280 34 4 89 9 27 78 2
221791686495: 277 239 608 8 8 3 4 9 2
29103234: 5 598 2 6 7 3 8 7 476 4
207714097130: 475 31 83 23 38 6 5
38394510: 1 2 8 1 57 474 510
345951420: 299 5 2 2 26 1 36 3 4 3 4
180653760: 929 2 9 700 8 4 7 9 435
1694660: 8 18 5 98 3 2 88 4 3 92
5847425: 2 7 230 9 248 8 83 2 1 5
699205954: 4 40 437 595 5
28421813066: 2 208 976 5 94 70 64 1
1298049029: 3 6 9 509 9 5 9 7 88 5 4 8
10881017840: 8 6 4 4 6 9 228 9 1 40 2 7
13016: 161 9 8 3 61
289861: 618 865 39 5 663 13
252140: 1 9 84 4 7 303 3 1 1 8 1 3
8221752: 91 5 949 79 792 7
1357: 19 4 9 6 667
3849872554: 1 2 6 11 478 188 8 554
973778: 9 73 358 2 5 413
7528: 7 66 8 39 14 2 7 6 4
117: 96 1 9 9 2
46777249: 997 8 586 27 21 8
2054: 827 586 75 562 4
4248057: 88 5 12 4 4 7 7
79721645787: 91 73 470 242 3 721 4
10660001: 704 8 28 3 7 2 94 5 6 1 2
107677328: 1 547 58 5 75 8 16
6349: 4 9 2 8 7 966 5 8 36 2 6 1
36947213778: 3 5 8 16 502 92 1 3 778
8631012248: 299 6 40 35 17 72 5
208032: 81 76 92 56 11 3
83119: 80 672 2 4 7 1 724 1
573218: 1 910 20 53 3
2604700: 4 6 2 35 70 610
702945093: 171 443 7 41 93
57834: 764 602 11 42
46881846: 4 688 1 84 7
169285: 69 3 75 75 9 8 4 1 9
37054280: 572 71 6 2 9 7 3 8 4 9 4 4
12822628: 5 41 9 3 9 885 3 5 8 3 4 7
290922: 8 66 91 3 6 3 937 371 2
12744811: 375 1 1 1 4 3 25 93 45
32672: 62 1 7 74 6 31 476 43
513955: 66 458 17 4 75
876662081: 81 6 66 620 81
5795667: 65 4 7 9 2 67 47 658 2 1
62238000: 3 34 70 91 3 23 34 264
3171462750: 9 8 72 4 991 96 5 186
45695000: 74 2 10 65 925
3084465: 513 1 6 4 65
98465646096: 324 5 19 3 39 778 88
292806360: 674 7 295 594 70
334523737: 8 53 1 5 25 5 5 7 58 4 9 2
9937740: 7 651 753 5 1 7 7 8 89 3
1780600: 626 4 8 387 7 7 8 45 90
84735810: 6 36 8 891 37 45 6 9 5
3626487097: 2 4 6 8 7 6 5 69 585 7 1 1
2140455: 885 7 82 341
4841376704: 942 270 9 7 45 47
1264329123: 52 302 97 1 83
1228: 3 65 2 8 69 9 2 662
949256812: 8 6 9 5 88 5 140 6 134 8
2309201829: 6 4 6 828 31 7 97 6 9
163463799328: 5 2 72 6 8 24 37 29 4 8
416218: 301 6 138 9
35109: 35 5 95 13 2 7
2068417: 45 27 4 9 798 1
2004726: 2 249 6 78 41 88
2779723056: 5 55 944 61 5 7
42747781453: 71 246 302 42 6
18000: 374 1 6 6 8
195332469: 54 255 48 7 316 31 9 4
179634324: 195 2 514 33 92
771: 1 34 4 1 61 252 9 411
7442949709: 81 9 7 3 6 5 2 999 5 2 3 6
11773758: 5 4 22 78 519 8 4 3 9 7 9
350110711613469: 962 620 73 52 8 7 587
41436044: 414 3 56 4 15 22 7
44694416: 2 72 43 5 99 7 1 3 25 2
13493114385: 613 1 131 57 4 42 9
316928718: 316 92 852 9 72 118
21971559166: 6 428 57 47 6 26 6 6 7 4
16108216155: 570 628 353 6 45
31218439520: 9 75 576 4 94 4 20
993: 2 93 43 102 3
67903: 611 110 679 6 8
16350: 162 725 8 990 89 2
300272: 750 7 9 392
2900257599: 9 7 9 5 29 1 2 7 9 5 7 598
29478343: 3 98 356 74
260606: 1 9 251 34 26 8
701121: 1 6 694 1 21
10246990323: 1 49 2 8 4 673 90 2 1 7
163889: 6 11 97 74 14 9
4572722859: 681 11 91 1 559 2 6
4045: 80 3 2 3 1 5
4903397761: 41 3 1 4 6 6 7 6 6 3 158 7
1416422: 56 29 36 694 8 59 6 1 2
39775104: 9 3 53 1 7 5 7 8 4 8 6 272
444776748: 63 1 3 3 4 4 7 4 8 91 996
3255727905: 7 1 7 5 5 2 6 9 438 790 5
8357: 801 6 82 259 3
112938766586: 415 216 136 6 4 5 5 86
757555928856: 12 7 1 3 45 901 88 4 8 8
329055496322: 57 9 1 4 596 8 4 1 2 4 8 1
42051: 8 3 30 889 159
220720500: 3 9 11 2 81 47 30 3 650
543098723: 18 10 295 6 22 6 3 21
549567: 10 687 2 63 45 681
1635199053: 1 3 7 4 23 8 5 4 34 78 4 9
10268240: 8 6 81 3 62 1 9 7 9 9 5 74
8192467009: 1 787 4 8 674 3 864 1
139192281: 592 149 3 526 57
16447098: 6 7 7 4 9 12 6 4 8 95 6 84
44075: 92 3 7 5 43
254239: 94 6 50 414 37 5 1
15819083175: 4 31 545 665 191
2243220: 41 96 56 1 99 4 319 2 6
2174: 750 5 6 587 83 740 3
3923217: 123 4 3 886 3 9
3970: 4 98 4 9 1
81933852: 3 9 3 4 219 51 7 8 6 627
343714356711: 92 4 934 2 356 711
47248532059: 684 30 4 82 702 6 852
55351277: 34 46 5 73 22 22
172962108: 5 77 583 9 6 67
49371: 80 41 136 3 3
3285241: 19 64 9 2 1 2 8 3 959 95
140798206: 732 9 4 24 96 2
1198087: 287 1 8 3 4 5 3 44 9 8 5 2
100807897: 2 621 7 3 7 552 7 1
324324: 68 9 14 44 81
1529910678048: 73 657 7 6 93 99 7 7
9519685562: 951 968 5 56 2
79194: 9 13 56 2 8 8 4 90
257796: 90 95 508 4 93
40269: 52 94 8 679 486
18462841531: 838 432 5 51 31
327603295042: 2 191 536 2 118 8 80 2
149050: 53 26 69 302 657 92
235063755: 587 6 57 40 7 949
11568655: 826 30 14 2 6 361 86
5523259696: 934 6 4 985 8 9 6 1 99 1
35933: 2 178 3 7 1 1 1 2 9 6 5 3
3508: 57 6 1 7 8
11576034: 3 8 2 229 3 3 8 1 51 3 27
711: 4 66 9 34 1 2 97
1890: 8 5 8 9 10
1050908860: 1 6 8 5 93 443 20
11656181041: 194 2 724 5 888 62 23"""

def check_equation(result, numbers, index, current_result):
    if len(numbers) == 0:
        return 1
    if index == len(numbers):
        return current_result == result

    # for the very 1st iteration
    if current_result is None:
        return check_equation(result, numbers, index + 1, numbers[index])

    return check_equation(result, numbers, index + 1, current_result + numbers[index]) \
        or check_equation(result, numbers, index + 1, current_result * numbers[index])

calibration = 0
for equation in puzzle_input.split("\n"):
    result, str_numbers = equation.split(": ")
    result = int(result)
    numbers = [int(x) for x in str_numbers.split(" ")]
    if check_equation(result, numbers, 0, None):
        calibration += result

print("Part 1: ", calibration)

def check_equation2(result, numbers, index, current_result):
    if index == len(numbers):
        return current_result == result

    # for the very 1st iteration
    if current_result is None:
        return check_equation2(result, numbers, index + 1, numbers[index])

    return check_equation2(result, numbers, index + 1, current_result + numbers[index]) \
        or check_equation2(result, numbers, index + 1, current_result * numbers[index]) \
        or check_equation2(result, numbers, index + 1, int(str(current_result) + str(numbers[index]))) \

calibration = 0
for equation in tqdm(puzzle_input.split("\n")):
    result, str_numbers = equation.split(": ")
    result = int(result)
    numbers = [int(x) for x in str_numbers.split(" ")]
    if check_equation2(result, numbers, 0, None):
        calibration += result

print("Part 2: ", calibration)
