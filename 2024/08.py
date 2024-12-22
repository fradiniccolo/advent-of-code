from itertools import permutations
from pprint import pprint

with open("08e.txt") as _:
    puzzle_input = _.read().strip()

print(puzzle_input)


rows = puzzle_input.split('\n')
map_size = len(rows)  # maps are square

antennas = {}
for row_idx, row in enumerate(rows):
    for char_idx, char in enumerate(row):
        if char != '.':
            coordinates = (char_idx, map_size-1-row_idx)
            if char not in antennas.keys():
                antennas[char] = [coordinates]
            else:
                antennas[char].append(coordinates)

print(antennas)


for frequency, coordinates in antennas.items():
    print(frequency)
    for combination in list(permutations(coordinates, 2)):
        print(combination)