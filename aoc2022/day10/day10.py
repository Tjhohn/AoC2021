# 20, 60, 100, 140, 180, 220
value_dict = {20 : 0, 60 : 0, 100 : 0, 140 : 0, 180 : 0, 220: 0}

def day10():
    cpu_cycle= 0
    x = 1
    with open('aoc2022/day10/input') as f:
        # each for is not a clock! as some instrctions tacke more so some need more than 1 for
        lines = f.readlines()

        for line in lines:
            lst = line.strip().split()
            if lst[0] == 'addx':
                cpu_cycle += 1
                cycle_cpu(cpu_cycle,x)
                cpu_cycle += 1
                cycle_cpu(cpu_cycle,x)
                x += int(lst[1])                 
            elif lst[0] == 'noop':
                cpu_cycle += 1
                cycle_cpu(cpu_cycle, x)

    print(value_dict)
    sum = 0
    for key in value_dict:
        sum += value_dict[key]
    print(sum)

def cycle_cpu(cycle, x):
    # check if in dict uand pdate dict if is
    if cycle in value_dict:
        value_dict[cycle] = cycle * x

def cycle_cpu_2(cycle, x):
    # check if in dict uand pdate dict if is
    if (cycle % 40) == x-1 or (cycle % 40) == x or (cycle % 40) == x+1:
        return '#'
    return ' '
    
def day10_2():
    # if x loc sprite is over sace on current cpu cycle fill out 
    cpu_cycle= -1
    x = 1
    screen = []
    with open('aoc2022/day10/input') as f:
        lines = f.readlines()

        for line in lines:
            lst = line.strip().split()
            if lst[0] == 'addx':
                cpu_cycle += 1
                screen.append(cycle_cpu_2(cpu_cycle,x))
                cpu_cycle += 1
                screen.append(cycle_cpu_2(cpu_cycle,x))
                x += int(lst[1])                 
            elif lst[0] == 'noop':
                cpu_cycle += 1
                screen.append(cycle_cpu_2(cpu_cycle, x))

    for i in range(0, 240, 40):
        print(''.join(screen[i:i+40]))


if __name__ == '__main__':
    print("day 10 result")
    day10()
    day10_2()