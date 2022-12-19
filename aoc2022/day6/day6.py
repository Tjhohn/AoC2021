def day6():
    letters = ''
    first = 0
    second = 0
    with open('aoc2022/day6/input') as f:
        lines = f.readlines()
        for i in range(0, len(lines[0])):
            letters += lines[0][i]
            if i > 3:
                if checkInput(i, letters) > 0 and first == 0:
                    first = i+1
            if i > 14:
                if checkInput2(i,letters) > 0:
                    second = i+1
                    break
        
    return first, second

def checkInput(i, letters):
    s = {letters[i], letters[i-1], letters[i-2],  letters[i-3]}
    if len(s) == 4:
        print(s)
        return 1
    return 0

def checkInput2(i, letters):
    s = {letters[i], letters[i-1], letters[i-2],  letters[i-3], letters[i-4], letters[i-5], letters[i-6],  letters[i-7],letters[i-8], letters[i-9], letters[i-10],  letters[i-11], letters[i-12], letters[i-13]}
    if len(s) == 14:
        print(s)
        return 1
    return 0

if __name__ == '__main__':
    print("day 6 result")
    print(day6())