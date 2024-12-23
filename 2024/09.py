from collections import deque

with open("09.txt") as _:
    puzzle_input = _.read().strip()

blocks = deque()
for index, char in enumerate(puzzle_input):
    if index%2 == 0:
        blocks += [index//2 for _ in range(int(char))]
    else:
        blocks += [None for _ in range(int(char))]

# filling moved_blocks while emptying blocks
moved_blocks = deque()
while blocks:
    current_left = blocks.popleft()
    if not current_left is None:
        moved_blocks.append(current_left)
    else:
        current_right = blocks.pop()
        while current_right is None:
            current_right = blocks.pop()
        moved_blocks.append(current_right)

checksum = 0
for index, number in enumerate(moved_blocks):
    checksum += index*number
print(checksum)