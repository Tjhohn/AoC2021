def day3():
    sum = 0
    sum2 = 0
    with open('aoc2022/day3/input') as f:
        lines = f.readlines()
        for line in lines:
            sum += line_sum(line)

        for i in range(len(lines)//3):
            line1 = lines[i *3 ].strip()
            line2 = lines[i*3 +1]
            line3 = lines[i*3 +2]
            sum2 += getPriority(getMatch( line1, line2, line3))



    return sum, sum2
        
def line_sum(line):
    part1 = line[:len(line)//2]
    part2 = line[len(line)//2:]

    for i in range(len(part1)):
        for c in part2:
            if c == part1[i]:
                return getPriority(c)

def getMatch(line1, line2, line3):
    match = list(set(line1).intersection(line2,line3))
    return match[0]

def getPriority(c):
    if ord(c) - 96 > 0:
        return ord(c) - 96
    else:
        return ord(c) - 38


if __name__ == '__main__':
    print("day 3 result")
    print(day3())  