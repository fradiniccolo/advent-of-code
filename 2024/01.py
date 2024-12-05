with open("2024/01.txt") as _:
    data = _.read().strip()

lists = [row.split('  ') for row in data.split('\n')]
list0, list1 = list(zip(*lists[::-1]))
list0 = sorted(list(map(int, list0)))
list1 = sorted(list(map(int, list1)))
differences = [abs(item0-item1) for item0, item1 in zip(list0, list1)]
part_one = sum(differences)

print(part_one)