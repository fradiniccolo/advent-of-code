class Warehouse:

    def __init__(self, file):
        self.size = None  # assuming square map
        self.items = []
        self.walls = []
        self.boxes = []
        self.robot = None
        self.initialise(file)

    def initialise(self, file):
        items, robot_moves = file.split('\n\n')
        robot_moves = robot_moves.replace('\n', '')
        for y, row in enumerate(items.split('\n')):
            for x, char in enumerate(row):
                if char == '#':
                    item = Wall(self, x, y)
                    self.walls.append(item)
                elif char == 'O':
                    item = Box(self, x, y)
                    self.boxes.append(item)
                elif char == '@':
                    self.robot = Robot(self, x, y, robot_moves)
        self.items += self.walls + self.boxes
        self.size = len(row)

    def simulate(self):
        for move in self.robot.moves:

            next = self.robot.get_next_item(move)
            if isinstance(next, type(None)):
                self.robot.move(move)
                continue

            queue = [next]
            if isinstance(next, Box):
                next = next.get_next_item(move)
                while isinstance(next, Box):
                    queue.append(next)
                    next = next.get_next_item(move)
                if isinstance(next, Wall):  # can't move
                    continue
                if isinstance(next, type(None)):
                    self.robot.move(move)
                    for item in queue:
                        item.move(move)
                    continue

    def __str__(self):
        map = [['.' for _ in range(self.size)]
               for _ in range(self.size)]
        map[self.robot.y][self.robot.x] = '@'
        for item in self.items:
            if isinstance(item, Wall):
                map[item.y][item.x] = '#'
            elif isinstance(item, Box):
                map[item.y][item.x] = 'O'
        return '\n'.join([''.join(row) for row in map])


class Item:

    def __init__(self, environment, x, y):
        self.environment = environment
        self.x = x
        self.y = y

    def __str__(self):
        return f"{type(self).__name__}{self.x, self.y}"

    def __repr__(self):
        return f"{type(self).__name__}{self.x, self.y}"

    def move_to_deltas(self, move):
        return {
            '>': (1, 0),
            '^': (0, -1),
            '<': (-1, 0),
            'v': (0, 1),
        }[move]

    def get_next_item(self, move):
        dx, dy = self.move_to_deltas(move)
        next_x = self.x + dx
        next_y = self.y + dy
        for item in self.environment.items:
            if next_x == item.x:
                if next_y == item.y:
                    return item

    def move(self, move):
        dx, dy = self.move_to_deltas(move)
        self.x += dx
        self.y += dy


class Robot(Item):

    def __init__(self, environment, x, y, moves=None):
        Item.__init__(self, environment, x, y)
        self.moves = moves


class Box(Item):

    def gps_coordinate(self):
        return 100*self.y + self.x


class Wall(Item):

    pass


with open("15.txt") as _:
    puzzle_input = _.read().strip()

warehouse = Warehouse(puzzle_input)

print('start')
print(warehouse, end='\n\n')

warehouse.simulate()

print('end')
print(warehouse, end='\n\n')
print(sum([box.gps_coordinate() for box in warehouse.boxes]))
