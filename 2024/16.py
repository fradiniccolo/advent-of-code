from heapq import heappop, heappush


def solve(text):
    start = None
    end = None
    for y, row in enumerate(text.split('\n')):
        for x, char in enumerate(row):
            if char == 'S':
                start = (x, y)
            elif char == 'E':
                end = (x, y)

    grid = text.replace('E', '.').split('\n')

    # directions counter-clockwise starting from (0, 1)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    directions.append(directions[0])
    turn_left = dict(zip(directions[:-1], directions[1:]))
    turn_right = dict(zip(directions[1:], directions[:-1]))

    heap = [(0, (1, 0), *start)]  # (score, direction_index, x, y)

    visited = set()
    while heap:
        cost, direction, x, y = heappop(heap)
        if (x, y) == end:
            break

        if (direction, x, y) in visited:
            continue

        visited.add((direction, x, y))

        # step forward, change coordinates
        dx, dy = direction
        step_x = x + dx
        step_y = y + dy
        if grid[step_y][step_x] == '.' and (direction, step_x, step_y) not in visited:
            heappush(heap, (cost + 1, direction, step_x, step_y))

        # turn left, change direction
        left = turn_left[direction]
        if (left, x, y) not in visited:
            heappush(heap, (cost + 1000, left, x, y))

        # turn right, change direction
        right = turn_right[direction]
        if (right, x, y) not in visited:
            heappush(heap, (cost + 1000, right, x, y))

    return cost


with open("16.txt") as _:
    puzzle_input = _.read().strip()

print(solve(puzzle_input))
