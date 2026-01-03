with open("06.txt", encoding="utf-8") as f:
    puzzle_input = f.read().strip()

*numbers, operations = puzzle_input.split("\n")
operations = operations.replace(" ", "")


def get_grand_total(numbers, operations):
    grand_total = 0
    for nums, op in zip(numbers, operations):
        total = nums[0]
        if op == "+":
            for num in nums[1:]:
                total += num
        else:
            for num in nums[1:]:
                total *= num
        grand_total += total
    return grand_total


# part 1
numbers_by_row = [
    [int(i) for i in row.split(" ") if i.isdigit()]
    for row in numbers
]
numbers_by_col = list(zip(*numbers_by_row))

grand_total_pt1 = get_grand_total(numbers_by_col, operations)
print(grand_total_pt1)

# part 2
numbers_transposed = [
    ''.join(n).strip() 
    for n in list(zip(*numbers))[::-1]
]
numbers_by_cephalopod = [[]]
for n in numbers_transposed:
    if n.isdigit():
        numbers_by_cephalopod[-1].append(int(n))
    else:
        numbers_by_cephalopod.append([])

grand_total_pt2 = get_grand_total(numbers_by_cephalopod, operations[::-1])
print(grand_total_pt2)
