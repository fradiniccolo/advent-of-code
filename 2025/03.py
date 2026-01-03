with open("03.txt", encoding="utf-8") as f:
    puzzle_input = f.read().strip()

banks = puzzle_input.split("\n")


def get_joltage_pt1(batteries):
    joltage = batteries[-2:]
    for index, first in enumerate(batteries[:-1]):
        for second in batteries[index + 1:]:
            if first + second > joltage:
                joltage = first + second
    return int(joltage)


def get_joltage_pt2(batteries):
    joltage = batteries
    while len(joltage) != 12:
        candidates = []
        for index in range(len(joltage)):
            candidates.append(joltage[:index] + joltage[index + 1:])
        joltage = max(candidates)
    return int(joltage)


max_capacity_pt1 = 0
max_capacity_pt2 = 0
for batteries in banks:
    max_capacity_pt1 += get_joltage_pt1(batteries)
    max_capacity_pt2 += get_joltage_pt2(batteries)


print(max_capacity_pt1)
print(max_capacity_pt2)
