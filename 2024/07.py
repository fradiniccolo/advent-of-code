with open("07.txt") as _:
    puzzle_input = _.read().strip()

equations = puzzle_input.split('\n')

equations = [equation.split(': ') for equation in equations]
equations = [(total, numbers.split()) for total, numbers in equations]
equations = [(int(total), tuple(map(int, numbers)))
             for total, numbers in equations]


def get_operators_combinations(operators_count):
    '''returns all the + and * operators combinations, obtained from a binary counter'''
    combinations = [
        f"{i:0{operators_count}b}"
        for i in range(2**operators_count)]
    combinations = [
        combination.replace('0', '+').replace('1', '*')
        for combination in combinations]
    return sorted(combinations, reverse=True)


def is_equation_true(equation):
    total, numbers = equation
    operators_count = len(numbers)-1
    operators_combinations = get_operators_combinations(operators_count)

    for combination in operators_combinations:
        result = numbers[0]
        for operator, number in zip(combination, numbers[1:]):
            result = eval(f"{result}{operator}{number}")
        if result == total:
            return True
        # elif result > total:
        #     return False
    return False


total_calibration = 0
for equation in equations:
    if is_equation_true(equation):
        total_calibration += equation[0]

print(total_calibration)
