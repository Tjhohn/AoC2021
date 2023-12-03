def part1(input):
    connected_sum = 0
    rows = len(input)
    cols = len(input[0]) if rows > 0 else 0
    checked_vales = set()

    for i in range(rows):
        for j in range(cols):
            if (i,j) in checked_vales:
                continue
            current = input[i][j]
            checked_vales.add((i,j))
            if not current.isdigit():
                continue
            num_indexs = [(i,j)]
            x = 1
            while input[i][j+x].isdigit():
                current += input[i][j+x]
                checked_vales.add((i,j+x))
                num_indexs.append((i,j+x))
                x +=1

            neighbors = []
            for index in num_indexs:
                first, second = index[0], index[1]
                if second - 1 >= 0:
                    neighbors.append(input[first][second - 1])
                if second + 1 < cols:
                    neighbors.append(input[first][second + 1])
                if first - 1 >= 0:
                    neighbors.append(input[first - 1][second])
                if first + 1 < rows:
                    neighbors.append(input[first + 1][second])
                if first - 1 >= 0 and second - 1 >= 0:
                    neighbors.append(input[first - 1][second - 1])
                if first - 1 >= 0 and second + 1 < cols:
                    neighbors.append(input[first - 1][second + 1])
                if first + 1 < rows and second - 1 >= 0:
                    neighbors.append(input[first + 1][second - 1])
                if first + 1 < rows and second + 1 < cols:
                    neighbors.append(input[first + 1][second + 1])

            for c in neighbors:
                if c in ['$', '@', '*', '+', '#', '+', '/', '%', '-', '&', '=']:
                    connected_sum += int(current)
                    break

    print(f"part one : {connected_sum}")

def part2(input):
    connected_sum = 0
    rows = len(input)
    cols = len(input[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            current = input[i][j]

            if current != '*':
                continue
            # good till here lol

            neighbors = []
            checked_values = set()
            first, second = i, j
            if second - 1 >= 0 and input[first][second - 1].isdigit() and (first,second) not in checked_values: # 4
                number, new_set = getNumber(input, (first,second - 1))
                neighbors.append(number)
                checked_values = checked_values.union(new_set)
            if second + 1 < cols and input[first][second + 1].isdigit(): # 5
                neighbors.append((first, second + 1))
            if first - 1 >= 0 and input[first - 1][second].isdigit(): # 2
                neighbors.append((first - 1, second))
            if first + 1 < rows and input[first + 1][second].isdigit(): # 7
                neighbors.append((first + 1,second))
            if first - 1 >= 0 and second - 1 >= 0 and input[first - 1][second - 1].isdigit(): # 1
                neighbors.append((first - 1, second - 1))
            if first - 1 >= 0 and second + 1 < cols and input[first - 1][second + 1].isdigit(): # 3
                neighbors.append((first - 1,second + 1))
            if first + 1 < rows and second - 1 >= 0 and input[first + 1][second - 1].isdigit(): # 6
                neighbors.append((first + 1, second - 1))
            if first + 1 < rows and second + 1 < cols and input[first + 1][second + 1].isdigit(): # 8
                neighbors.append((first + 1, second + 1))

            # if neighbors:
            #     value_list = set()
            #     for indices in neighbors:
            #         input_list = input[indices[0]]
            #         index = indices[1]
            #         result = input_list[index]
            #         i = index + 1
            #         while i < len(input_list) and input_list[i].isdigit():
            #             result += input_list[i]
            #             i += 1
            #
            #         # Move backward from the given index
            #         i = index - 1
            #         while i >= 0 and input_list[i].isdigit():
            #             result = input_list[i] + result
            #             i -= 1
            #
            #         value_list.add(int(result))
            #
            #     if len(value_list) < 2 or len(value_list) > 2:
            #         continue
            #     value_list = list(value_list)

                connected_sum += (value_list[0] * value_list[1])

    print(f"part two : {connected_sum}") # should be 80703636

def getNumber(input , indices):
    input_list = input[indices[0]]
    index = indices[1]
    result = input_list[index]
    check_set = set()
    check_set.add(indices)
    i = index + 1
    while i < len(input_list) and input_list[i].isdigit():
        result += input_list[i]
        check_set.add((indices[0],i))
        i += 1

    # Move backward from the given index
    i = index - 1
    while i >= 0 and input_list[i].isdigit():
        result = input_list[i] + result
        check_set.add((indices[0],i))
        i -= 1

    return result, check_set

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()
    with open('testinput') as f:
        testinput = f.readlines()
    part1(testinput)
    part1(lines)
    part2(testinput)
    part2(lines)
