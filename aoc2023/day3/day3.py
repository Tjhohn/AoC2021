def part1(input):
    for line in input:
        pass

    print(f"part one : {1}")

def part2(input):
    for line in input:
        pass

    print(f"part two : {1}")


if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()
    testinput = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
             "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
             "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
             "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
             "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", ]
    part1(testinput)
    part1(lines)
    part2(testinput)
    part2(lines)
