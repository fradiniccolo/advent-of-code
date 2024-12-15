puzzle_input = \
"""
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip()


# with open("06.txt") as _:
#     puzzle_input = _.read().strip()


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
        self.direction = (0,1)
        self.steps = 0
    
    def obstacle_in_front(self):
        delta_x, delta_y = self.direction
        return (self.x + delta_x, self.y + delta_y) in obstacles
    
    def move_one_step(self):
        delta_x, delta_y = self.direction
        self.x += delta_x
        self.y += delta_y
        self.steps += 1

    def turn(self):
        directions = ((0,1), (1,0), (0,-1), (-1,0))
        current_direction_index = directions.index(self.direction)
        next_direction_index = (current_direction_index+1)%4
        self.direction = directions[next_direction_index]
        
    def is_on_map(self):
        if self.x >= map_size or self.x < 0:
            return False
        if self.y >= map_size or self.y < 0:
            return False
        return True
    


# main loop
from time import sleep

guard = Guard(*guard_initial_position)

while guard.is_on_map():
    print(guard.x, guard.y)
    sleep(0.05)
    if guard.obstacle_in_front():
        guard.turn()
        continue
    guard.move_one_step()
    

# for obst_x, obst_y in obstacles:



print(guard.steps)