with open("01.txt", encoding="utf-8") as f:
    puzzle_input = f.read().strip()

instructions = puzzle_input.replace("L", "-").replace("R", "").split("\n")
instructions = list(map(int, instructions))

current = 50
count = 0
for instruction in instructions:
    current += instruction
    current %= 100
    if current == 0:
        count += 1
print(count)

current = 50
count = 0
for instruction in instructions:
    step = -1 if instruction < 0 else 1
    for _ in range(abs(instruction)):
        current += step
        current %= 100
        if current == 0:
            count += 1
print(count)
