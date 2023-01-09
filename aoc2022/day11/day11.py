import copy


class Monkey:
    part2=1

    def __init__(self, items, inspect, check, divisor=1):
        self.items = items
        self.inspection_count= 0
        self.inspect_func = inspect
        self.check_func = check
        Monkey.part2 *=divisor

    def add_item(self, item):
        self.items.append(item)

    def inspect(self):
        self.items[0] = self.inspect_func(self.items[0])
        self.inspection_count +=1 

    def bored(self):
        self.items[0] = self.items[0] // 3

    def managed(self):
        self.items[0] = self.items[0] % Monkey.part2 # Chinese remainder theorem, its hard to wrap head around 

    def test(self):
        item = self.items.pop(0)
        return (item, self.check_func(item))

    def __repr__(self):
        return f"items: {self.items} cnt: {self.inspection_count}"

def create_operation(op, second_value):
    if op == "*":
        return lambda x: x * (x if second_value == "old" else int(second_value))

    return lambda x: x + (x if second_value == "old" else int(second_value))

def create_test(val, true, false):
    return lambda x :  true if x % val == 0 else false

def day11():
    
    monkeys = []
    with open('aoc2022/day11/input') as f:
        lines = f.readlines()

    blocks = ''.join(lines).split("\n\n")
    for monkey in blocks:
        monk = monkey.split('\n')

        vals = list(map(int, monk[1].split(': ')[1].split(', ')))

        op = monk[2].split(' = old')[1].split()
        test = int(monk[3].split(' by ')[1])
        truthy = int(monk[4].split(' monkey ')[1])
        falsey = int(monk[5].split(' monkey ')[1])

        # print(vals, '\n', op, '\n', test,'\n', truthy,'\n', falsey)

        monkeys.append(Monkey(vals, create_operation(op[0], op[1]), create_test(test, truthy, falsey), test))

    partOne(copy.deepcopy(monkeys))
    partTwo(monkeys)
    


def partOne(monkeys):
    for i in range(20):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                monkey.inspect()
                monkey.bored()
                item, loc = monkey.test()
                monkeys[loc].add_item(item)
    
    monkeys.sort(key = lambda x : x.inspection_count, reverse=True)
    print(monkeys[0].inspection_count * monkeys[1].inspection_count)

def partTwo(monkeys):
    for i in range(10_000):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                monkey.inspect()
                monkey.managed()
                item, loc = monkey.test()
                monkeys[loc].add_item(item)
    
    monkeys.sort(key = lambda x : x.inspection_count, reverse=True)
    print(monkeys[0].inspection_count * monkeys[1].inspection_count)    

if __name__ == '__main__':
    print("day 11 result")
    day11()