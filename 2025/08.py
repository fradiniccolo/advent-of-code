from itertools import combinations
from collections import deque

threshold = 10
with open("08e.txt", encoding="utf-8") as f:
    puzzle_input = f.read().strip()

coords = [
    tuple(map(int, coord.split(",")))
    for coord in puzzle_input.splitlines()
]


def square_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)


combo_dists = deque()
for combo in combinations(coords, 2):
    dist = square_distance(combo[0], combo[1])
    combo_dists.append((combo, dist))

combo_dists = sorted(combo_dists, key=lambda x: x[1])


circuits = deque([set(combo_dists[0][0])])
for combo, dist in combo_dists[1:threshold+1]:
    found = False
    for circuit in circuits:
        if any(coord in circuit for coord in combo):
            circuit.update(combo)
            found = True
            break
    if not found:
        circuits.append(set(combo))

circuits = sorted(circuits, key=lambda x: -len(x), reverse=False)

# for c in circuits:
#     print(c)

sizes = [len(circuit) for circuit in circuits]

result = sizes[0]
for s in sizes[1:3]:
    result *= s


print(result)

# 3276 too low