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

            neighbors = []
            first, second = i, j
            if second - 1 >= 0 and input[first][second - 1].isdigit():
                neighbors.append((first,second - 1))
            if second + 1 < cols and input[first][second + 1].isdigit():
                neighbors.append((first, second + 1))
            if first - 1 >= 0 and input[first - 1][second].isdigit():
                neighbors.append((first - 1, second))
            if first + 1 < rows and input[first + 1][second].isdigit():
                neighbors.append((first + 1,second))
            if first - 1 >= 0 and second - 1 >= 0 and input[first - 1][second - 1].isdigit():
                neighbors.append((first - 1, second - 1))
            if first - 1 >= 0 and second + 1 < cols and input[first - 1][second + 1].isdigit():
                neighbors.append((first - 1,second + 1))
            if first + 1 < rows and second - 1 >= 0 and input[first + 1][second - 1].isdigit():
                neighbors.append((first + 1, second - 1))
            if first + 1 < rows and second + 1 < cols and input[first + 1][second + 1].isdigit():
                neighbors.append((first + 1, second + 1))

            # im handling this wrong as may have 2 neighbors that are from same number!
            if len(neighbors) >= 2:
                row_set = set()
                col_set = set()

                value_list = set()
                for indices in neighbors:
                    input_list = input[indices[0]]
                    index = indices[1]
                    result = input_list[index]
                    i = index + 1
                    while i < len(input_list) and input_list[i].isdigit():
                        result += input_list[i]
                        i += 1

                    # Move backward from the given index
                    i = index - 1
                    while i >= 0 and input_list[i].isdigit():
                        result = input_list[i] + result
                        i -= 1

                    value_list.add(int(result))

                temp_sum = 1

                for val in value_list:
                    temp_sum = temp_sum * val

                connected_sum += temp_sum

    print(f"part two : {connected_sum}") # not 74956339



if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()
    with open('testinput') as f:
        testinput = f.readlines()
    part1(testinput)
    part1(lines)
    part2(testinput)
    part2(lines)
