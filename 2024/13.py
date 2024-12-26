import re


class Machine:

    def __init__(self, ax, ay, bx, by, px, py):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.px = px
        self.py = py

    def __repr__(self):
        return f"A{self.ax, self.ay} B{self.bx, self.by} P{self.px, self.py}"

    def is_winnable(self):

        # lines starting from (0, 0) and (px, py)
        # with directions (ax, ay) and (bx, by)
        # should intersect on integer coordinates

        # let's find the intersecting point

        # slopes:
        ma = self.ay/self.ax
        mb = self.by/self.bx

        # line point-slope form:
        # y - y1 = m(x - x1)

        # origin, slope a:
        # y - 0 = ma(x - 0)
        # ->  y = ma*x

        # prize, slope b:
        # y - self.py = mb*(x - self.px)
        # -> y - self.py = mb*x - mb*self.px

        # combine line equations by subtracting:
        # y - self.py - (y) = mb*x - mb*self.px - (ma*x)
        # -> -self.py = x*(mb-ma) - mb*self.px
        # -> x*(ma-mb) = self.py - mb*self.px
        # -> x = (self.py - mb*self.px)/(ma-mb)

        # this is the coordinate x of the intersection point
        int_x = (self.py - mb*self.px)/(ma-mb)

        button_a = round(int_x/self.ax, 9)
        button_b = round((self.px-int_x)/self.bx, 9)

        if button_a.is_integer():
            if button_b.is_integer():
                return int(button_a), int(button_b)

    def cost(self):
        if self.is_winnable():
            button_a, button_b = self.is_winnable()
            return button_a*3 + button_b


with open("13.txt") as _:
    puzzle_input = _.read().strip()

machines = []
for specs in puzzle_input.split('\n\n'):
    numbers = list(map(int, re.findall('\d+', specs)))
    machines.append(Machine(*numbers))
    print(machines[-1], '\n', machines[-1].is_winnable(),
          ':', machines[-1].cost(), end='\n\n')

print(sum([machine.cost() for machine in machines if machine.cost()]))
