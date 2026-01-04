with open("07e.txt", encoding="utf-8") as f:
    puzzle_input = f.read().strip()

# print(puzzle_input)

width = len(puzzle_input.splitlines()[0])
height = len(puzzle_input.splitlines())

room_map = {}
for index, char in enumerate(puzzle_input.replace("\n", "")):
    x = index % width
    y = index // width
    room_map[(x, y)] = char

entrance = [pos for pos, char in room_map.items() if char == "S"][0]
splitters = [pos for pos, char in room_map.items() if char == "^"]

split_positions = set()
visited_positions = set()


def beam_step(position):
    global split_positions, visited_positions
    if position in visited_positions:
        return
    visited_positions.add(position)

    x, y = position

    below = (x, y + 1)
    cell = room_map.get(below)

    if cell == ".":
        beam_step(below)

    elif cell == "^":
        beam_step((x - 1, y + 1))
        beam_step((x + 1, y + 1))
        split_positions.add(below)

    return


beam_step(entrance)

split_count = len(split_positions)
print(split_count)
