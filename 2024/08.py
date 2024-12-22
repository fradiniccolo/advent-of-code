from itertools import permutations

with open("08.txt") as _:
    puzzle_input = _.read().strip()


rows = puzzle_input.split('\n')
map_size = len(rows)  # maps are square, width = height -> size

antenna_groups = {}
for row_idx, row in enumerate(rows):
    for char_idx, char in enumerate(row):
        if char != '.':
            antennas = (char_idx, map_size-1-row_idx)
            if char not in antenna_groups.keys():
                antenna_groups[char] = []
            antenna_groups[char].append(antennas)


def is_pt_on_map(pt):
    x, y = pt
    return 0 <= x < map_size and 0 <= y < map_size


def get_antinodes(antennas, resonant):
    antinodes = []
    for pta, ptb in list(permutations(antennas, 2)):
        dx = pta[0] - ptb[0]
        dy = pta[1] - ptb[1]
        step = 1 - int(resonant)  # if resonant, start from 0 to count antennas
        while True:
            ptc = (pta[0]+step*dx, pta[1]+step*dy)
            ptd = (ptb[0]-step*dx, ptb[1]-step*dy)
            if is_pt_on_map(ptc):
                antinodes.append(ptc)
            if is_pt_on_map(ptd):
                antinodes.append(ptd)
            if not resonant:
                break
            if not is_pt_on_map(ptc) and not is_pt_on_map(ptd):
                break
            step += 1
    return antinodes


def get_antinodes_groups(antenna_groups, resonant=False):
    antinode_groups = {}
    for frequency, antennas in antenna_groups.items():
        antinode_groups[frequency] = get_antinodes(antennas, resonant)
    return antinode_groups


def get_unique_antinodes(antinode_groups):
    unique_antinodes = set()
    for group in antinode_groups.values():
        for pt in group:
            unique_antinodes.add(pt)

    return unique_antinodes


antinode_groups = get_antinodes_groups(antenna_groups)
print(len(get_unique_antinodes(antinode_groups)))

antinode_groups = get_antinodes_groups(antenna_groups, resonant=True)
print(len(get_unique_antinodes(antinode_groups)))
