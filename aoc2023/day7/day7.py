def part1(input):
    for line in input:
        pass

    print(f"part one : {0}")

def part2(input):
    for line in input:
        pass

    print(f"part two : {0}")


if __name__ == '__main__':
    with open('input') as f:
        out = f.readlines()
    hands = []
    for line in out:
        hand, bid = line.split(" ")
        hands.append((hand, int(bid)))

    with open('testinput') as f:
        testinput = f.readlines()

    test_hands = []
    for line in out:
        hand, bid = line.split(" ")
        test_hands.append((hand, int(bid)))

    part1(test_hands)
    part1(hands)
    part2(test_hands)
    part2(hands)
