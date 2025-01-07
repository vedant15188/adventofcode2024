import numpy as np
import re

puzzle_input = """............0.......................Bn...........v
.........0.....................8.........P.....D..
........M...........Q..0..8...h.......P...........
......M.A......c...................n..............
.....C..................A.........................
.M.AC....................................v........
........C..........W...w....J........Q...........y
.....i..............0.....nW.......w.Zv...6.......
........c....................A.........Pm........D
.............t.........x..........P....y....m.....
........................w...x.......F....Z........
...............Q......x6.......S......Z..O.......J
..............o.u........x....6.....r.D..M........
............c...o........u...Y....................
.........i............9..............g............
.....................d..WC..8.........J.g.........
...........X.c...............d...........m........
....................9.dR...........m......y.......
.............o.....9.......Y.6.OS...n..........F..
......i..................a..Q...r.Y.............U.
.....N......X......u..Ot...a......j......7........
..........q..X......t.....uH.......j.r..S.7.......
..........l...t....K.......................J......
...............9..............OB..................
...l.R...q..............g.......Y.7..V.......S....
..........................a.D............V........
......R.5...v.....W.............KB............U...
........Kp..F.N...........2.....B..............U..
..............................d..........h........
...L...NX...l...R...w..........F...........7......
..q.L......5.........................j............
.q.............5.......g..4.......................
............p...................s2..............Z.
......L...p...........................s..I........
........N..............................H..........
............5......................2.......hV.....
.............3..........1.......f.a...V...........
.....K..................................Hz....j...
.............k.b..G................I.....U........
.............1......................h.............
...........p...........L.....s....4T..............
.b..................G....s.T......I...............
............................H...........T4........
...............lk.................T...............
..i........................1........Iz............
..............b...........1........G..............
....b..............G..............................
........3......k............f..............4......
3.............k.2.....................z...........
...........3......................z..f............"""

split = puzzle_input.split("\n")

# 2d numpy array for the puzzle input
grid = np.array([list(line) for line in split])

# 2d numpy array of zeros for tracking anti-nodes
anti_node_grid = np.zeros((len(split), len(split[0])), dtype=int)

frequencies = list(set(re.findall(r"\d|[a-z]|[A-Z]", puzzle_input)))

def add_anti_nodes(locations, anti_node_grid):
    checked = []
    for i in range(len(locations)):
        for j in range(len(locations)):
            if i != j and (sorted([i, j]) not in checked):
                a = locations[i]
                b = locations[j]
                checked.append(sorted([i, j]))

                diff = a - b
                an1 = a + diff
                an2 = b - diff

                if 0 <= an1[0] < len(anti_node_grid) and 0 <= an1[1] < len(anti_node_grid[0]):
                    anti_node_grid[an1[0], an1[1]] = 1
                if 0 <= an2[0] < len(anti_node_grid) and 0 <= an2[1] < len(anti_node_grid[0]):
                    anti_node_grid[an2[0], an2[1]] = 1
    return anti_node_grid

for freq in frequencies:
    locations = np.argwhere(grid == freq)
    anti_node_grid = add_anti_nodes(locations, anti_node_grid)

print("Part 1: ", np.sum(anti_node_grid))

# Reinitialize the anti-node grid for part 2
anti_node_grid = np.zeros((len(split), len(split[0])), dtype=int)

def add_anti_nodes2(locations, anti_node_grid):
    checked = []
    for i in range(len(locations)):
        for j in range(len(locations)):
            if i != j and (sorted([i, j]) not in checked):
                # Have multiplier cover both sides of the coordinate distance
                multiplier = range(-100, 100)
                for m in multiplier:
                    a = locations[i]
                    b = locations[j]
                    checked.append(sorted([i, j]))

                    diff = (a - b) * m
                    an1 = a + diff
                    an2 = b - diff

                    if 0 <= an1[0] < len(anti_node_grid) and 0 <= an1[1] < len(anti_node_grid[0]):
                        anti_node_grid[an1[0], an1[1]] = 1
                    if 0 <= an2[0] < len(anti_node_grid) and 0 <= an2[1] < len(anti_node_grid[0]):
                        anti_node_grid[an2[0], an2[1]] = 1

    return anti_node_grid

for freq in frequencies:
    locations = np.argwhere(grid == freq)
    anti_node_grid = add_anti_nodes2(locations, anti_node_grid)

print("Part 2: ", np.sum(anti_node_grid))
