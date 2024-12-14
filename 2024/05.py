# puzzle_input = \
# """
# 47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13

# 75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47
# """.strip()


with open("05.txt") as _:
    puzzle_input = _.read().strip()


rules, updates = puzzle_input.split('\n\n')

rules = [
    list(map(int, item.split('|')))
    for item in rules.split('\n')
]

not_to_be_followed_by = {}

for value, key in rules:
    if key not in not_to_be_followed_by.keys():
        not_to_be_followed_by[key] = set([value])
    else:
        not_to_be_followed_by[key].add(value)


updates = [
    list(map(int, item.split(',')))
    for item in updates.split('\n')
]


def check_update(update):
    for index, page in enumerate(update):
        if index+1 < len(update) and page in not_to_be_followed_by.keys():
            remaining_pages = set(update[index+1:])
            if not_to_be_followed_by[page] & remaining_pages:
                return
    return update[len(update)//2]


middle_values = [middle_value for update in updates if (
    middle_value := check_update(update)) is not None]

print(sum(middle_values))
