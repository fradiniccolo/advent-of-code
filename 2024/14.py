from time import sleep
import os


class Environment:

    def __init__(self, width, height, robot_info=None):
        self.width = width
        self.height = height
        self.robots = []
        if robot_info:
            self.populate_from_robot_info(robot_info)

    def populate_from_robot_info(self, robot_info):
        for row in robot_info.split('\n'):
            position, velocity = row.split()
            px, py = map(int, position[2:].split(','))
            vx, vy = map(int, velocity[2:].split(','))
            self.robots.append(Robot(self, px, py, vx, vy))

    def simulate(self, *, seconds=100):
        for second in range(seconds+1):
            
            os.system('clear')
            
            if second:
                for robot in self.robots:
                    robot.move()
                    
            map = [['.' for _ in range(self.width)]
                   for _ in range(self.height)]

            robot_locations = {}
            for robot in self.robots:
                location = (robot.px, robot.py)
                if location not in robot_locations.keys():
                    robot_locations[location] = 1
                else:
                    robot_locations[location] += 1

            for (x, y), robot_count in robot_locations.items():
                map[y][x] = str(robot_count)

            print('\n'.join(''.join(row) for row in map))

            # sleep(0.5)

    def get_safety_factor(self):
        quadrants = {}
        for robot in self.robots:
            if robot.px != self.width//2 and robot.py != self.height//2:
                qx = robot.px//(self.width//2+1)
                qy = robot.py//(self.height//2+1)
                if (qx, qy) not in quadrants.keys():
                    quadrants[(qx, qy)] = 1
                else:
                    quadrants[(qx, qy)] += 1
        safety_factor = 1
        for value in quadrants.values():
            safety_factor *= value
        return safety_factor, quadrants


class Robot:

    def __init__(self, environment, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.environment = environment

    def __repr__(self):
        return f"Robot(p={self.px, self.py}, v={self.vx, self.vy})"

    def __str__(self):
        return f"Robot(p={self.px, self.py}, v={self.vx, self.vy})"

    def move(self):
        self.px += self.vx
        self.py += self.vy
        self.px = self.px % environment.width
        self.py = self.py % environment.height


with open("14.txt") as _:
    puzzle_input = _.read().strip()

if len(puzzle_input.split('\n')) < 20:
    environment = Environment(11, 7, puzzle_input)
else:
    environment = Environment(101, 103, puzzle_input)
environment.simulate()
print(environment.get_safety_factor())
