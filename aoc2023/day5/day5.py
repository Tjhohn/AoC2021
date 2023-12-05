def part1(input):
    seeds, maps = parse_input(input)

    for conversion_map in maps:
        next_numbers = []
        for number in seeds:
            converted_number = apply_map(number, conversion_map)
            next_numbers.append(converted_number)

        seeds = next_numbers

    print(f"part one : {min(seeds)}")

def part2(input):
    sum = 0
    for line in input:
        pass

    print(f"part two : {sum}")

def apply_map(number, map):
    for dest_start, source_start, length in map:
        if source_start <= number < source_start + length:
            return dest_start + (number - source_start)
    return number

def parse_input(input):
    seeds = list(input[0].split(":")[1].strip().split(" "))
    seeds = [int(x) for x in seeds ]
    index = 3
    seed_to_soil =[]
    while input[index] != "\n":
        temp = input[index].strip().split()
        temp = tuple([ int(x) for x in temp])
        seed_to_soil.append(temp)
        index +=1

    index +=2
    soil_to_fert =[]
    while input[index] != "\n":
        temp = input[index].strip().split()
        temp = tuple([ int(x) for x in temp])
        soil_to_fert.append(temp)
        index += 1
    index +=2

    fert_to_water = []
    while input[index] != "\n":
        temp = input[index].strip().split()
        temp = tuple([ int(x) for x in temp])
        fert_to_water.append(temp)
        index += 1
    index +=2

    wawa_to_light = []
    while input[index] != "\n":
        temp = input[index].strip().split()
        temp = tuple([ int(x) for x in temp])
        wawa_to_light.append(temp)
        index += 1
    index +=2

    light_to_temp = []
    while input[index] != "\n":
        temp = input[index].strip().split()
        temp = tuple([ int(x) for x in temp])
        light_to_temp.append(temp)
        index += 1
    index +=2

    temp_to_hum = []
    while input[index] != "\n":
        temp = input[index].strip().split()
        temp = tuple([ int(x) for x in temp])
        temp_to_hum.append(temp)
        index += 1

    index +=2
    hum_to_loc = []
    while index < len(input):
        temp = input[index].strip().split()
        temp = tuple([ int(x) for x in temp])
        hum_to_loc.append(temp)
        index += 1

    return seeds, [seed_to_soil, soil_to_fert, fert_to_water, wawa_to_light, light_to_temp, temp_to_hum, hum_to_loc]




if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()
    with open('testinput') as f:
        testinput = f.readlines()
    part1(testinput)
    part1(lines)
    part2(testinput)
    part2(lines)
