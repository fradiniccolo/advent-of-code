with open("07.txt") as _:
    puzzle_input = _.read().strip()

equations = puzzle_input.split('\n')
equations = [equation.split(': ') for equation in equations]
equations = [(total, numbers.split()) for total, numbers in equations]
equations = [(int(total), list(map(int, numbers)))
             for total, numbers in equations]


def calculate(first, operator, second):
    if operator == '||':
        return eval(f"{first}{second}")
    return eval(f"{first}{operator}{second}")


def is_equation_true(test_value, numbers, operators):
    if len(numbers) == 2:
        first, second = numbers
        for operator in operators:
            result = calculate(first, operator, second)
            if result > test_value:  # save computation
                continue
            if result == test_value:
                return True
        return False
    else:
        first, second = numbers[:2]
        remaining = numbers[2:]
        for operator in operators:
            result = calculate(first, operator, second)
            if result > test_value:  # save computation
                continue
            less_numbers = [result] + remaining
            if is_equation_true(test_value, less_numbers, operators):
                return True
    return False


operators = ['+', '*']
total_calibration = 0
for test_value, numbers in equations:
    if is_equation_true(test_value, numbers, operators):
        total_calibration += test_value

print(total_calibration)


operators = ['+', '*', '||']
total_calibration = 0
for test_value, numbers in equations:
    if is_equation_true(test_value, numbers, operators):
        total_calibration += test_value

print(total_calibration)
