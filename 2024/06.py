import os
from time import sleep

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
        self.visited_pts = [(self.x, self.y)]
        self.turning_pts = []

    def is_facing_obstacle(self):
        dx, dy = self.direction
        return (self.x + dx, self.y + dy) in obstacles

    def move_one_step(self):
        dx, dy = self.direction
        self.x += dx
        self.y += dy
        if self.is_on_map():
            self.visited_pts.append((self.x, self.y))

    def turn(self):
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        current_direction_index = directions.index(self.direction)
        next_direction_index = (current_direction_index+1) % 4
        self.direction = directions[next_direction_index]
        self.turning_pts.append((self.x, self.y))
        

    def is_on_map(self):
        if not 0 <= self.x < map_size or not 0 <= self.y < map_size:
            return False
        return True

    def display(self):
        # sleep(0.05)
        # os.system("clear")
        map = [['.' for char in range(map_size)] for row in range(map_size)]
        for obst_x, obst_y in obstacles:
            map[map_size-1-obst_y][obst_x] = '#'
        for vis_x, vis_y in self.visited_pts:
            map[map_size-1-vis_y][vis_x] = '∘'
        guard_fig = {(0, 1): '^', (1, 0): '>', (0, -1): 'v', (-1, 0): '<'}
        try:
            map[map_size-1-self.y][self.x] = guard_fig[self.direction]
        except:
            pass
        map = '\n'.join([''.join(row) for row in map])
        print(map)


guard = Guard(*guard_initial_position)


def get_candidate_turning_pt(obj):
    if len(obj.turning_pts) >= 3:
        triad = obj.turning_pts[-3:]
        xs, ys = zip(*triad)
        xs = sorted(list(xs))
        xs.remove(xs.pop(1))
        ys = sorted(list(ys))
        ys.remove(ys.pop(1))
        return *xs, *ys
    return None


options_count = 0
while guard.is_on_map():
    guard.display()
    print(options_count, 'options so far')
    if guard.is_facing_obstacle():
        guard.turn()
    guard.move_one_step()
    if get_candidate_turning_pt(guard) == (guard.x, guard.y):
        options_count += 1
    
print(len(set(guard.visited_pts)))
print(options_count)