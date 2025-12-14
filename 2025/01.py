with open("01.txt", encoding="utf-8") as f:
    puzzle_input = f.read().strip()

instructions = puzzle_input.split("\n")

current = 50
count = 0
for instruction in instructions:
    if instruction[0] == "L":
        current -= int(instruction[1:])
    else:
        current += int(instruction[1:])
    current %= 100
    if current == 0:
        count += 1
print(count)

current = 50
count = 0
for instruction in instructions:
    step = -1 if instruction[0] == "L" else 1
    for _ in range(int(instruction[1:])):
        current += step
        current %= 100
        if current == 0:
            count += 1
print(count)