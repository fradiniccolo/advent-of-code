class Environment:

    def __init__(self, width, height, robot_info=None):
        self.width = width
        self.height = height
        self.robots = []
        self.populate_from_robot_info(robot_info)

    def populate_from_robot_info(self, robot_info):
        if robot_info:
            for row in robot_info.split('\n'):
                position, velocity = row.split()
                px, py = map(int, position[2:].split(','))
                vx, vy = map(int, velocity[2:].split(','))
                self.robots.append(Robot(self, px, py, vx, vy))

    def simulate(self, *, seconds=100, easter_egg_search=False):

        def search_for_easter_egg():
            import numpy as np
            from PIL import Image

            # empty image
            image = np.zeros((self.height, self.width), dtype=np.uint8)

            # draw
            for robot in self.robots:
                if image[robot.py][robot.px] == 0:
                    image[robot.py][robot.px] = 1
                else:
                    # assuming there shouldn't be robots on the same tile
                    return
            image *= 255
            image = Image.fromarray(image, mode='L')
            image.save(f'14-{second}.png')

            return second

        for second in range(seconds+1):
            if second:
                for robot in self.robots:
                    robot.move()
            if easter_egg_search:
                easter_egg_second = search_for_easter_egg()
                if easter_egg_second:
                    return easter_egg_second
        return self

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
        return safety_factor


class Robot:

    def __init__(self, environment, px, py, vx, vy):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.environment = environment

    def move(self):
        self.px += self.vx
        self.py += self.vy
        self.px = self.px % environment.width
        self.py = self.py % environment.height


with open("14.txt") as _:
    puzzle_input = _.read().strip()

environment = Environment(101, 103, puzzle_input)
print(environment.simulate().get_safety_factor())

environment = Environment(101, 103, puzzle_input)
print(environment.simulate(seconds=10000, easter_egg_search=True))
