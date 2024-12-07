import re

with open("04.txt") as _:
    puzzle_input = _.read().strip()

# puzzle_input = """
# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# """.strip()

xmas_count = 0

# horizontal search
xmas_count += len(re.findall('XMAS', puzzle_input))
xmas_count += len(re.findall('XMAS'[::-1], puzzle_input))

# vertical search
flipped_input = [[char for char in row] for row in puzzle_input.split('\n')]
flipped_input = list(zip(*flipped_input))
flipped_input = [''.join(row) for row in flipped_input]
flipped_input = '\n'.join([''.join(row) for row in flipped_input])

xmas_count += len(re.findall('XMAS', flipped_input))
xmas_count += len(re.findall('XMAS'[::-1], flipped_input))

# diagonal search
rows = puzzle_input.split('\n')
size = len(rows)
primary_diagonals = ['' for _ in range(2 * size - 1)]
secondary_diagonals = ['' for _ in range(2 * size - 1)]

for i in range(size):
    for j in range(size):
        primary_diagonals[i + j] += rows[i][j]
        secondary_diagonals[i - j + (size - 1)] += rows[i][j]

diagonals = primary_diagonals + secondary_diagonals
diagonals = '\n'.join(diagonals)

xmas_count += len(re.findall('XMAS', diagonals))
xmas_count += len(re.findall('XMAS'[::-1], diagonals))

print(xmas_count)
