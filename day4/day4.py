class Board:
    def __init__(self, rows=5, cols=5):
        self.array = [] * cols
        self.won = False

    def print(self):
        print(self.array)

    def update(self, value):
        for row in range(5):
            for col in range(5):
                if self.array[row][col] == value:
                    self.array[row][col] = '0'

    def check_if_won(self):
        if self.array[0][0] == '0' and self.array[0][1] == '0' and self.array[0][2] == '0' and self.array[0][3] == '0' and self.array[0][4] == '0':
            return True
        if self.array[1][0] == '0' and self.array[1][1] == '0' and self.array[1][2] == '0' and self.array[1][3] == '0' and self.array[1][4] == '0':
            return True
        if self.array[2][0] == '0' and self.array[2][1] == '0' and self.array[2][2] == '0' and self.array[2][3] == '0' and self.array[2][4] == '0':
            return True
        if self.array[3][0] == '0' and self.array[3][1] == '0' and self.array[3][2] == '0' and self.array[3][3] == '0' and self.array[3][4] == '0':
            return True
        if self.array[4][0] == '0' and self.array[4][1] == '0' and self.array[4][2] == '0' and self.array[4][3] == '0' and self.array[4][4] == '0':
            return True

        if self.array[0][0] == '0' and self.array[1][0] == '0' and self.array[2][0] == '0' and self.array[3][0] == '0' and self.array[4][0] == '0':
            return True
        if self.array[0][1] == '0' and self.array[1][1] == '0' and self.array[2][1] == '0' and self.array[3][1] == '0' and self.array[4][1] == '0':
            return True
        if self.array[0][2] == '0' and self.array[1][2] == '0' and self.array[2][2] == '0' and self.array[3][2] == '0' and self.array[4][2] == '0':
            return True
        if self.array[0][3] == '0' and self.array[1][3] == '0' and self.array[2][3] == '0' and self.array[3][3] == '0' and self.array[4][3] == '0':
            return True
        if self.array[0][0] == '0' and self.array[1][4] == '0' and self.array[2][4] == '0' and self.array[3][4] == '0' and self.array[4][4] == '0':
            return True

        if self.array[0][0] == '0' and self.array[1][1] == '0' and self.array[2][2] == '0' and self.array[3][3] == '0' and self.array[4][4] == '0':
            return True
        if self.array[0][4] == '0' and self.array[1][3] == '0' and self.array[2][2] == '0' and self.array[3][1] == '0' and self.array[4][0] == '0':
            return True

        else:
            return False

    def sum_board(self):
        total = 0
        for row in range(5):
            for col in range(5):
                if self.array[row][col] != '0':
                    total += int(self.array[row][col])

        return total


if __name__ == '__main__':
    filename = "day4input.txt"
    print("Day 4\n")
    file = open(filename, "r")
    nums = file.readline().split(',')

    #test = Board()
    # for x in range(5):
    #     test.array.append(['0', '0', '0', '0', '0'],)
    #     test.array.append(['0', '1', '2', '3', '4'])
    #
    # test.array.append(['0', '1', '0', '0', '0'])
    # test.array.append(['0', '0', '0', '1', '0'])
    # test.array.append(['1', '0', '0', '1', '0'])
    # test.array.append(['0', '0', '0', '0', '1'])
    # test.array.append(['0', '1', '0', '0', '0'])
    #
    # print(test.check_if_won())
    # test.update('4')
    # test.print()
    # print(test.sum_board())
    # test.update('2')
    # test.print()
    # print(test.sum_board())

    print(nums)
    boards = []
    have_won = []
    for board in range(100):
        board = Board()
        file.readline()  # remove empty before each board
        for i in range(5):
            line = file.readline().rstrip().split()
            board.array.append(line)

        boards.append(board)
    found = False
    for called_num in nums:
        i = 0
        for board in boards:
            board.update(called_num)
            if board.check_if_won():
                if not found:
                    print('part 1:' ,board.sum_board() * int(called_num))
                    found = True
                    board.won = True
                    have_won.append(i)
                else:
                    if not board.won:
                        board.won = True
                        have_won.append(i)
                        if len(have_won) == 100:
                            print('part 2:', board.sum_board() * int(called_num))
                            break
            i += 1
