
def day1(input):
    part_one_sum = 0

    for line in input:
        digits = [c for c in line if c.isdigit()]

        num = digits[0] + digits[-1]
        part_one_sum += int(num)

    print(f"part 1 : {part_one_sum}")


def part2(input):
    part_two_sum = 0
    for line in input:
        digit_mapping = {
            'one': '1', 'two': '2', 'three': '3',
            'four': '4', 'five': '5', 'six': '6',
            'seven': '7', 'eight': '8', 'nine': '9'
        }
        for spelled_digit in digit_mapping.keys():
            line = line.replace(spelled_digit, spelled_digit + digit_mapping[spelled_digit] + spelled_digit)

        digits = [c for c in line if c.isdigit()]

        num = digits[0] + digits[-1]
        part_two_sum += int(num)
    print(f"part 2 : {part_two_sum}")


if __name__ == '__main__':
    print("day 1 result")
    with open('input') as f:
        lines = f.readlines()
    day1(lines)
    part2(lines)
