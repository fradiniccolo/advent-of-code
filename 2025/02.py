from itertools import batched

with open("02.txt", encoding="utf-8") as f:
    puzzle_input = f.read().strip().replace("\n", "")


def is_id_valid_pt1(number):
    number = str(number)
    if len(number) % 2 != 0:
        return True
    mid = len(number) // 2
    return number[:mid] != number[mid:]


def is_id_valid_pt2(number):
    number = str(number)
    if len(set(number)) == 1 and len(number) > 1:
        return False
    mid = len(number) // 2
    for partition_length in range(2, mid + 1):
        if len(number) % partition_length != 0:
            continue
        if len(set(batched(number, partition_length))) == 1:
            return False
    return True


invalid_ids_sum_pt1 = 0
invalid_ids_sum_pt2 = 0
for product_id in puzzle_input.split(","):
    start, end = map(int, product_id.split("-"))
    for current in range(start, end + 1):
        if not is_id_valid_pt1(current):
            invalid_ids_sum_pt1 += current
        if not is_id_valid_pt2(current):
            invalid_ids_sum_pt2 += current

print(invalid_ids_sum_pt1)
print(invalid_ids_sum_pt2)
