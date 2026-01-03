with open("04.txt", encoding="utf-8") as f:
    puzzle_input = f.read().strip()


def get_adjacent_items(row_index, col_index, diagram):
    rows = diagram.splitlines()
    size = len(rows)
    result = ''
    for r in range(max(0, row_index - 1), min(size, row_index + 2)):
        for c in range(max(0, col_index - 1), min(size, col_index + 2)):
            # Skip the item itself
            if r == row_index and c == col_index:
                continue
            result += rows[r][c]
    return result


def count_adjacent_rolls(row_index, col_index, diagram):
    roll_count = 0
    for item in get_adjacent_items(row_index, col_index, diagram):
        if item == '@':
            roll_count += 1
    return roll_count


def make_roll_count_diagram(diagram):
    size = len(diagram.splitlines())
    roll_count_diagram = ''
    for r in range(size):
        for c in range(size):
            roll_count_diagram += str(count_adjacent_rolls(r, c, diagram))
        roll_count_diagram += '\n'
    return roll_count_diagram.strip()


def make_removable_rolls_diagram(diagram):
    roll_count_diagram = make_roll_count_diagram(diagram)
    removable_rolls_diagram = ''
    for i, (d, p) in enumerate(zip(roll_count_diagram, puzzle_input)):
        if p == '.':
            removable_rolls_diagram += '.'
        elif p == '\n':
            removable_rolls_diagram += '\n'
        elif d < '4':
            removable_rolls_diagram += 'x'
        else:
            removable_rolls_diagram += '@'
    return removable_rolls_diagram


def get_removable_rolls_count(diagram):
    count = 0
    for i in diagram:
        if i == 'x':
            count += 1
    return count


old_iteration = None
new_iteration = make_removable_rolls_diagram(puzzle_input)

# print(new_iteration)
print(get_removable_rolls_count(new_iteration))

while True:
    old_iteration = new_iteration
    new_iteration = make_removable_rolls_diagram(old_iteration)
    
    if old_iteration == new_iteration:
        break

    # print(new_iteration)
    
print(get_removable_rolls_count(new_iteration))
