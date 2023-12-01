import copy

filename = 'input-11.txt'
monkeys = []

"""
We'll do GCD for Chinese Remainder Theorem
"""
MONKEY_DIVISOR_CONSTANT = 1

with open(filename, 'r') as file:
    for m in file.read().strip().split('\n\n'):
        monkey = {'inspected': 0}
        for instruction in m.split('\n'):
            match instruction.strip().split():
                case ['Monkey', n]:
                    monkey['name'] = int(n.split(':')[0])
                case ['Starting', _, *items]:
                    monkey['items'] = list(map(lambda x: int(x.replace(',', '')), items))
                case ['Operation:', _, _, _, op, n]:
                    monkey['operation'] = [op, n]
                case ['Test:', _, _, n]:
                    MONKEY_DIVISOR_CONSTANT *= int(n)    # find GCD, divisors are prime
                    monkey['test'] = int(n)
                case ['If', 'true:', _, _, _, n]:
                    monkey['test_true'] = int(n)
                case ['If', 'false:', _, _, _, n]:
                    monkey['test_false'] = int(n)
                case _:
                    quit(1)
        monkeys.append(monkey)


def do_operation(operation, old, new):
    match operation:
        case '+':
            return old + new
        case '-':
            return old - new
        case '*':
            return old * new
        case _:
            quit(1)


def solve(data, iteration, divide=True):
    global MONKEY_DIVISOR_CONSTANT
    for _ in range(iteration):
        for monkey in data:
            if len(monkey['items']) == 0:
                continue
            for item in monkey['items']:
                item = do_operation(monkey['operation'][0], item,
                                    int(monkey['operation'][1]) if monkey['operation'][1] != 'old' else item)

                if divide:
                    item //= 3
                else:
                    item %= MONKEY_DIVISOR_CONSTANT    # Apply CRT to reduce computational time and power

                if item % monkey['test'] == 0:
                    data[monkey['test_true']]['items'].append(item)
                else:
                    data[monkey['test_false']]['items'].append(item)

                monkey['items'] = monkey['items'][1:]
                monkey['inspected'] += 1
    print(type(data))
    data.sort(key=lambda x: x['inspected'], reverse=True)
    return data[0]['inspected'] * data[1]['inspected']


m1 = copy.deepcopy(monkeys)
m2 = copy.deepcopy(monkeys)
print(f'Part 1: %d' % solve(m1, 20))
print(f'Part 2: %d ' % solve(m2, 10000, False))