def part1(input):
    num_red = 12
    num_green = 13
    num_blue = 14
    valid_id_sum = 0
    for line in input:
        game, values = line.split(':')
        game = int(game.split(' ')[1])
        turns = values.split(';')
        invalid = False
        for turn in turns:
            if invalid:
                break
            pulls = turn.split(',')
            for pull in pulls:
                pull = pull.strip()
                val, color = pull.split(' ')
                if color == 'red':
                    if int(val) > num_red:
                        invalid = True
                        break
                if color == 'blue':
                    if int(val) > num_blue:
                        invalid = True
                        break
                if color == 'green':
                    if int(val) > num_green:
                        invalid = True
                        break

        if not invalid:
            valid_id_sum += game

    print(f"part one : {valid_id_sum}")
def part2(input):

    power_sum = 0
    for line in input:
        game, values = line.split(':')
        game = int(game.split(' ')[1])
        turns = values.split(';')
        num_red = 0
        num_green = 0
        num_blue = 0
        for turn in turns:
            pulls = turn.split(',')
            for pull in pulls:
                pull = pull.strip()
                val, color = pull.split(' ')
                if color == 'red':
                    if int(val) > num_red:
                        num_red = int(val)
                if color == 'blue':
                    if int(val) > num_blue:
                        num_blue = int(val)
                if color == 'green':
                    if int(val) > num_green:
                        num_green = int(val)

        power_sum += (num_red * num_blue * num_green)

    print(f"part two : {power_sum}")


if __name__ == '__main__':
    print("result")
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
