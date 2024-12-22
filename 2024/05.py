with open("05.txt") as _:
    puzzle_input = _.read().strip()


def get_mid_value(lst):
    return lst[len(lst)//2]


def check_update(update):
    for index, page in enumerate(update):
        if index+1 < len(update) and page in not_to_be_followed_by.keys():
            remaining_pages = set(update[index+1:])
            intersection = not_to_be_followed_by[page] & remaining_pages
            if intersection:
                return False, (index, list(intersection)[0])
    return True, (None, None)


def sort_update(update):
    while True:
        result, (index_a, intersection) = check_update(update)
        if result:
            return update
        else:
            index_b = update.index(intersection)
            update[index_a], update[index_b] = update[index_b], update[index_a]


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

middle_values = [
    get_mid_value(update) for update in updates
    if check_update(update)[0]
]

print(sum(middle_values))

sorted_updates = [
    sort_update(update) for update in updates
    if not check_update(update)[0]
]

middle_values = [
    get_mid_value(update) for update in sorted_updates
]

print(sum(middle_values))
