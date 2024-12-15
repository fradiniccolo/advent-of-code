# puzzle_input = \
# """
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# """.strip()


with open("06.txt") as _:
    puzzle_input = _.read().strip()


# turn map in 2d domain
rows = puzzle_input.split('\n')
map_size = len(rows)  # maps are square

obstacles = []
guard_initial_position = None
for row_idx, row in enumerate(rows):
    for char_idx, char in enumerate(row):
        # turn obstacles into coordinates
        if char == '#':
            obstacles.append((char_idx, map_size-1-row_idx))
        # turn guard into coordinates
        elif char == '^':
            guard_initial_position = [char_idx, map_size-1-row_idx]

# build class Guard


class Guard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = (0, 1)
        self.visited = [(self.x, self.y)]

    def obstacle_in_front(self):
        delta_x, delta_y = self.direction
        return (self.x + delta_x, self.y + delta_y) in obstacles

    def move_one_step(self):
        delta_x, delta_y = self.direction
        self.x += delta_x
        self.y += delta_y
        if self.is_on_map():
            self.visited.append((self.x, self.y))

    def turn(self):
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        current_direction_index = directions.index(self.direction)
        next_direction_index = (current_direction_index+1) % 4
        self.direction = directions[next_direction_index]

    def is_on_map(self):
        if self.x >= map_size or self.x < 0:
            return False
        if self.y >= map_size or self.y < 0:
            return False
        return True


guard = Guard(*guard_initial_position)


def display():
    map = [['.' for char in range(map_size)] for row in range(map_size)]
    for obst_x, obst_y in obstacles:
        map[map_size-1-obst_y][obst_x] = '#'
    for vis_x, vis_y in guard.visited:
        map[map_size-1-vis_y][vis_x] = '∘'
    map[map_size-1-guard.y][guard.x] = '^'
    map = '\n'.join([''.join(row) for row in map])
    print(map)


while guard.is_on_map():
    # os.system("clear")
    # display()
    # sleep(0.05)
    if guard.obstacle_in_front():
        guard.turn()
        continue
    guard.move_one_step()


print(len(set(guard.visited)))
# print(guard.visited)


def get_path_corners():
    corners = [guard.visited[0]]
    for step0, step1, step2 in zip(guard.visited[:-2], guard.visited[1:-1], guard.visited[2:]):
        if len(set((step0[0], step1[0], step2[0]))) < 3 \
                and len(set((step0[1], step1[1], step2[1]))) < 3:
            corners.append(step1)
    return corners


def get_rectangle_missing_corner(corner0, corner1, corner2):
    xs, ys = zip(corner0, corner1, corner2)
    xs = sorted(list(xs))
    xs.remove(xs.pop(1))
    ys = sorted(list(ys))
    ys.remove(ys.pop(1))
    return xs[0], ys[0]


def does_it_intersect_obstacles(corner0, corner1, corner2, corner3):
    rect_corners = [corner0, corner1, corner2, corner3]
    for corner_start, corner_end in zip(rect_corners+[rect_corners[0]], [rect_corners[-1]] + rect_corners):
        if corner_start[0] == corner_end[0]:
            lower_bound = min(corner_start[1], corner_end[1])
            upper_bound = max(corner_start[1], corner_end[1])
            if any([
                corner_start[0] == obstacle[0] and
                lower_bound < obstacle[1] < upper_bound
                for obstacle in obstacles]
            ):
                return True
        else:
            lower_bound = min(corner_start[0], corner_end[0])
            upper_bound = max(corner_start[0], corner_end[0])
            if any([
                corner_start[1] == obstacle[1] and
                lower_bound < obstacle[0] < upper_bound
                for obstacle in obstacles]
            ):
                return True
    return False


corners = get_path_corners()

rectangles = []
rectangle_count = 0
for triad in zip(corners[:-2], corners[1:-1], corners[2:]):
    rectangle_corners = list(triad) + [get_rectangle_missing_corner(*triad)]
    # print(rectangle_corners)
    if not does_it_intersect_obstacles(*rectangle_corners):
        print(rectangle_corners)
        rectangle_count += 1

print(rectangle_count)


# 48
