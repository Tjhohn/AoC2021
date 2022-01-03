# --- Day 3: Binary Diagnostic ---
# The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.
#
# The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine. The first parameter to check is the power consumption.
#
# You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate). The power consumption can then be found by multiplying the gamma rate by the epsilon rate.
#
# Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report. For example, given the following diagnostic report:
#
# 00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010
# Considering only the first bit of each number, there are five 0 bits and seven 1 bits. Since the most common bit is 1, the first bit of the gamma rate is 1.
#
# The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.
#
# The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.
#
# So, the gamma rate is the binary number 10110, or 22 in decimal.
#
# The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal. Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.
#
# Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together. What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
#
# Your puzzle answer was 2261546.
#
# The first half of this puzzle is complete! It provides one gold star: *
#
# --- Part Two ---
# Next, you should verify the life support rating, which can be determined by multiplying the oxygen generator rating by the CO2 scrubber rating.
#
# Both the oxygen generator rating and the CO2 scrubber rating are values that can be found in your diagnostic report - finding them is the tricky part. Both values are located using a similar process that involves filtering out values until only one remains. Before searching for either rating value, start with the full list of binary numbers from your diagnostic report and consider just the first bit of those numbers. Then:
#
# Keep only numbers selected by the bit criteria for the type of rating value for which you are searching. Discard numbers which do not match the bit criteria.
# If you only have one number left, stop; this is the rating value for which you are searching.
# Otherwise, repeat the process, considering the next bit to the right.
# The bit criteria depends on which type of rating value you want to find:
#
# To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered.
# To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered.
# For example, to determine the oxygen generator rating value using the same example diagnostic report from above:
#
# Start with all 12 numbers and consider only the first bit of each number. There are more 1 bits (7) than 0 bits (5), so keep only the 7 numbers with a 1 in the first position: 11110, 10110, 10111, 10101, 11100, 10000, and 11001.
# Then, consider the second bit of the 7 remaining numbers: there are more 0 bits (4) than 1 bits (3), so keep only the 4 numbers with a 0 in the second position: 10110, 10111, 10101, and 10000.
# In the third position, three of the four numbers have a 1, so keep those three: 10110, 10111, and 10101.
# In the fourth position, two of the three numbers have a 1, so keep those two: 10110 and 10111.
# In the fifth position, there are an equal number of 0 bits and 1 bits (one each). So, to find the oxygen generator rating, keep the number with a 1 in that position: 10111.
# As there is only one number left, stop; the oxygen generator rating is 10111, or 23 in decimal.
# Then, to determine the CO2 scrubber rating value from the same example above:
#
# Start again with all 12 numbers and consider only the first bit of each number. There are fewer 0 bits (5) than 1 bits (7), so keep only the 5 numbers with a 0 in the first position: 00100, 01111, 00111, 00010, and 01010.
# Then, consider the second bit of the 5 remaining numbers: there are fewer 1 bits (2) than 0 bits (3), so keep only the 2 numbers with a 1 in the second position: 01111 and 01010.
# In the third position, there are an equal number of 0 bits and 1 bits (one each). So, to find the CO2 scrubber rating, keep the number with a 0 in that position: 01010.
# As there is only one number left, stop; the CO2 scrubber rating is 01010, or 10 in decimal.
# Finally, to find the life support rating, multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.
#
# Use the binary numbers in your diagnostic report to calculate the oxygen generator rating and CO2 scrubber rating, then multiply them together. What is the life support rating of the submarine? (Be sure to represent your answer in decimal, not binary.)
#


def split_apart(charcters):
    return [char for char in charcters]


def majority_at(list_array, location):
    cnt = 0
    for item in list_array:
        if item[location] == '1':
            cnt += 1
        else:
            cnt -= 1

    if cnt > 0:
        return 1
    else:
        return 0

def part1(filename):
    f = open(filename, "r")
    gamma, epsilon = "", ""
    oxy_list, co2_list = [], []
    value_list = [0] * 12

    for line in f:
        arr = split_apart(line)
        for x in range(12):
            digit = arr[x]
            if digit == '1':
                value_list[x] = value_list[x] + 1
            else:
                value_list[x] = value_list[x] - 1

    for n in value_list:
        if n > 0:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    f = open(filename, "r")
    if value_list[0] > 0:
        for line in f:
            if line.startswith('1'):
                oxy_list += [line]
            else:
                co2_list += [line]
    else:
        for line in f:
            if line.startswith('0'):
                oxy_list += [line]
            else:
                co2_list += [line]

    while len(oxy_list) > 2:
        for x in range(1, 12):
            temp_list = []
            for item in oxy_list:
                if value_list[x] > 0:
                    if item[x] == '1':
                        temp_list.append(item)
                else:
                    if item[x] == '0':
                        temp_list.append(item)
            oxy_list = temp_list
            if len(oxy_list) == 1:
                break

    return int(gamma,2) * int(epsilon,2)




def line_toString_bit(line_toProcess):
    # Used in part One
    return sum(2 ** pos * value for pos, value in enumerate(line_toProcess))


def transform_data(list_zeros, list_ones):
    # Used in partOne
    final_ganmma = line_toString_bit([1 if x > y else 0 for x, y in zip(list_ones, list_zeros)])
    final_epsilon = line_toString_bit([1 if x < y else 0 for x, y in zip(list_ones, list_zeros)])

    print(f'Final ganma {final_ganmma}')
    print(f'Final epsilon {final_epsilon}')
    print(f'Final epsilon {final_ganmma * final_epsilon}')
    return -1


def get_number_bits(fd):
    # Part One
    line_lenght = None
    for line in fd:
        if not line_lenght:
            line_lenght = len(line)
            list_zeros = [0] * line_lenght
            list_ones = [0] * line_lenght
        line_bit = [int(x) for x in line.strip()]
        for pos, bit in enumerate(line_bit[::-1]):
            if bit:
                list_ones[pos] += 1
            else:
                list_zeros[pos] += 1

    transform_data(list_zeros, list_ones)
    return 1


def get_bitCriteria(list_arrayBits, pos):
    # This function will return the most common/uncommon bit for a position
    # that is specifid in pos
    # if most_common=true , gets the most_common bit
    bit_counter = 0
    for bit_array in list_arrayBits:
        if bit_array[pos]:
            bit_counter += 1

    # Return 1 if there are more 1
    return 1 if bit_counter >= ((len(list_arrayBits) + 1) // 2) else 0


def get_filter_criteria(fd, max):
    #  if max = 1
    #  take the most common

    all_lines = [[int(x) for x in line.strip()] for line in fd.readlines()]
    line_lenght = len(all_lines[0])
    oxigen_value = []

    # Get oxigen Value
    for i in range(line_lenght):
        if len(all_lines) > 1:
            mc_bit = get_bitCriteria(all_lines, i)  # Get most common bit
            if max:
                all_lines = list(filter(lambda arraybit: arraybit[i] == mc_bit, all_lines))  # Filter the new list
            else:
                mc_bit = 0 if mc_bit else 1
                all_lines = list(filter(lambda arraybit: arraybit[i] == mc_bit, all_lines))
            oxigen_value.append(mc_bit)
        else:
            oxigen_value.append(all_lines[0][i])

    print("I'm on get_filter_criteria")
    return oxigen_value




if __name__ == '__main__':
    file_name_challenge = "input.txt"
    print("Day 3\n")
    print("result one: " ,part1("input.txt"))


    objetiveOxigen_bitarray = get_filter_criteria(open(file_name_challenge, "r"), True)
    objetiveOxigen_value = line_toString_bit(objetiveOxigen_bitarray[::-1])

    print(f'This is the result - BIT STRING - {objetiveOxigen_bitarray} - VALUE - {objetiveOxigen_value} ')
    objetiveC02_bitarray = get_filter_criteria(open(file_name_challenge, "r"), False)
    objetiveC02_value = line_toString_bit(objetiveC02_bitarray[::-1])

    print(f'This is the result - BIT STRING - {objetiveC02_bitarray} - VALUE - {objetiveC02_value} ')

    print(f'This is the result - multiplied {objetiveOxigen_value * objetiveC02_value} ')
