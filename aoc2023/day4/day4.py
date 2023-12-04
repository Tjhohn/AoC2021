def part1(input):
    sum = 0
    for line in input:
        winners, chances = line.strip().split('|')
        winners = winners.split(':')[1]
        winners = winners.split(' ')
        winners = [i for i in winners if i]
        chances = chances.split(' ')
        chances = [i for i in chances if i]
        matches = 0
        for chance in chances:
            if chance.strip() in winners:
                matches += 1

        if matches != 0:
            sum += 2 ** (matches - 1)

    print(f"part one : {sum}")

def part2(input):
    sum = 0
    shortcut_dict = {}
    ticket_count = {1 : 0}
    for line in input:
        winners, chances = line.split('|')
        game = winners.split(':')[0].strip().split(" ")[-1].strip()
        winners = winners.strip().split(':')[1]
        winners = winners.split(' ')
        winners = [i for i in winners if i]
        chances = chances.strip().split(' ')
        chances = [i for i in chances if i]
        matches = 0
        for chance in chances:
            if chance.strip() in winners:
                matches += 1


        if matches != 0:
            # add the squential matches
            tickets = ticket_count.get(int(game),-1)
            for _ in range(tickets+1):
                start_index = int(game)
                index = int(game)
                while index < (start_index + matches):
                    ticket_count[index+1] = ticket_count.get(index+1, 0) + 1
                    index += 1

    total_sum = 0
    for key in ticket_count:
        total_sum += ticket_count[key]

    print(f"part two : {total_sum  + len(input)}") # not 52512522, 3412105 4060424 too low


if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()
    with open('testinput') as f:
        testinput = f.readlines()
    part1(testinput)
    part1(lines)
    part2(testinput)
    part2(lines)
