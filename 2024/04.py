import re

with open("04.txt") as _:
    puzzle_input = _.read().strip()


class Puzzle:

    def __init__(self, puzzle_text):
        self.rows = puzzle_text.split('\n')
        self.columns = [''.join(col) for col in zip(*self.rows)]
        self.size = len(self.rows[0])

        # Calculate diagonals
        rows = self.rows
        primary_diagonals = ['' for _ in range(2 * self.size - 1)]
        secondary_diagonals = ['' for _ in range(2 * self.size - 1)]

        for row in range(self.size):
            for col in range(self.size):
                primary_diagonals[row + col] += rows[row][col]
                secondary_diagonals[row - col +
                                    (self.size - 1)] += rows[row][col]

        self.diagonals = primary_diagonals + secondary_diagonals

    def count_xmas(self):
        unfolded_text = '\n'.join([
            '\n'.join(self.rows),
            '\n'.join(self.columns),
            '\n'.join(self.diagonals),
        ])
        xmas_count = len(re.findall('XMAS', unfolded_text))
        xmas_count += len(re.findall('XMAS'[::-1], unfolded_text))
        return xmas_count

    def get_x_strokes(self, row_index, col_index):
        square = [
            self.rows[row_index - 1][col_index - 1:col_index + 2],
            self.rows[row_index][col_index - 1:col_index + 2],
            self.rows[row_index + 1][col_index - 1:col_index + 2],
        ]
        return [
            f"{square[0][0]}{square[1][1]}{square[2][2]}",
            f"{square[0][2]}{square[1][1]}{square[2][0]}",
        ]

    def count_x_mas(self):
        xmas_count = 0
        for row_index in range(1, self.size - 1):
            for col_index in range(1, self.size - 1):
                strokes = self.get_x_strokes(row_index, col_index)
                if all(stroke in ['MAS', 'SAM'] for stroke in strokes):
                    xmas_count += 1
        return xmas_count


puzzle = Puzzle(puzzle_input)


print(puzzle.count_xmas())
print(puzzle.count_x_mas())
