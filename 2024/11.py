from collections import deque

with open("11.txt") as _:
    puzzle_input = _.read().strip()


stones = [int(stone) for stone in puzzle_input.split()]


def blink(stone):
    if stone == 0:
        return 1
    len_digits = len(str(stone))
    if len_digits % 2 == 0:
        halves = [
            int(str(stone)[:len_digits//2]),
            int(str(stone)[len_digits//2:]),
        ]
        return halves
    return stone*2024


for _ in range(25):
    changing_stones = deque()
    for stone in stones:
        new_stone = blink(stone)
        if isinstance(new_stone, list):
            changing_stones += new_stone
        else:
            changing_stones.append(new_stone)
    stones = changing_stones
print(len(stones))
