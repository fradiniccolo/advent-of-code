from itertools import product


with open("07.txt") as _:
    puzzle_input = _.read().strip()

equations = puzzle_input.split('\n')
equations = [equation.split(': ') for equation in equations]
equations = [(total, numbers.split()) for total, numbers in equations]
equations = [(int(total), tuple(map(int, numbers)))
             for total, numbers in equations]


def get_operators_combinations(operators, operators_count):
    combinations = list(product(operators, repeat=operators_count))
    order = {key: value for value, key in enumerate(['+', '*', '||'])}
    order = sorted(combinations, key=lambda o: order.get(o, float('inf')))
    order.reverse()
    # print(order)
    return order


def is_equation_true(equation, operators):
    total, numbers = equation
    operators_count = len(numbers)-1
    operators_combinations = get_operators_combinations(
        operators, operators_count)

    for combination in operators_combinations:
        result = numbers[0]
        for operator, number in zip(combination, numbers[1:]):
            if operator != '||':
                result = eval(f"{result}{operator}{number}")
            else:
                result = eval(f"{result}{number}")
            if result > total:
                # return False
                break
        if result == total:
            return True
    return False


operators = ['+', '*']
total_calibration = 0
for equation in equations:
    if is_equation_true(equation, operators):
        total_calibration += equation[0]

print(total_calibration)


operators = ['+', '*', '||']
total_calibration = 0
for equation in equations:
    if is_equation_true(equation, operators):
        total_calibration += equation[0]

print(total_calibration)

# 12839601725877