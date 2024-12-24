with open("11.txt") as _:
    puzzle_input = _.read().strip()


class Stone:

    stone_count = 0

    def __init__(self, number, *, blink_count=0, max_blinks):
        Stone.stone_count += 1
        self.number = number
        self.blink_count = blink_count
        self.max_blinks = max_blinks
        self.blink()

    def get_next(self):
        if self.number == 0:
            return [1]
        number_digits = len(str(self.number))
        if number_digits % 2 == 0:
            return [
                int(str(self.number)[:number_digits//2]),
                int(str(self.number)[number_digits//2:]),
            ]
        return [self.number*2024]

    def blink(self):
        if self.blink_count < self.max_blinks:
            Stone.stone_count -= 1
            for number in self.get_next():
                Stone(number, blink_count=self.blink_count +
                      1, max_blinks=self.max_blinks)


stones = [Stone(int(item), max_blinks=25) for item in puzzle_input.split()]
print(Stone.stone_count)

stones = [Stone(int(item), max_blinks=75) for item in puzzle_input.split()]
print(Stone.stone_count)
