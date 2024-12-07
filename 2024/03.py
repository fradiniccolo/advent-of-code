import re

with open("03.txt") as _:
    puzzle_input = _.read().strip().replace('\n', '')

# find `mul(...)` matches
matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", puzzle_input)

result = 0
for match in matches:
    a, b = map(int, match[4:-1].split(','))
    result += a*b

print(result)

# remove instructions between don't() and do()
only_enabled = ''.join(re.split(r"don't\(\).*?do\(\)", puzzle_input))

# remove remaining `don't()`s
only_enabled = re.split(r"don't\(\).*", only_enabled)[0]

matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", only_enabled)

result = 0
for match in matches:
    a, b = map(int, match[4:-1].split(','))
    result += a*b

print(result)
