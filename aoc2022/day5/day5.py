#                     [L]     [H] [W]
#                 [J] [Z] [J] [Q] [Q]
# [S]             [M] [C] [T] [F] [B]
# [P]     [H]     [B] [D] [G] [B] [P]
# [W]     [L] [D] [D] [J] [W] [T] [C]
# [N] [T] [R] [T] [T] [T] [M] [M] [G]
# [J] [S] [Q] [S] [Z] [W] [P] [G] [D]
# [Z] [G] [V] [V] [Q] [M] [L] [N] [R]
#  1   2   3   4   5   6   7   8   9 
stack1 = ['Z', 'J', 'N','W','P','S']
stack2 = ['G','S','T']
stack3 = ['V','Q','R','L','H']
stack4 = ['V','S','T','D']
stack5 = ['Q','Z','T','D','B','M','J']
stack6 = ['M','W','T','J','D','C','Z','L']
stack7 = ['L','P','M','W','G','T','J']
stack8 = ['N','G','M','T','B','F','Q','H']
stack9 = ['R','D','G','C','P','B','Q','W']

def fillStacks():
    global stack1
    stack1 = ['Z', 'J', 'N','W','P','S']
    global stack2 
    stack2 = ['G','S','T']
    global stack3
    stack3 = ['V','Q','R','L','H']
    global stack4
    stack4 = ['V','S','T','D']
    global stack5
    stack5 = ['Q','Z','T','D','B','M','J']
    global stack6
    stack6 = ['M','W','T','J','D','C','Z','L']
    global stack7
    stack7 = ['L','P','M','W','G','T','J']
    global stack8
    stack8 = ['N','G','M','T','B','F','Q','H']
    global stack9
    stack9 = ['R','D','G','C','P','B','Q','W']

def day5():

    with open('aoc2022/day5/input') as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split(sep=',')
            how_many=data[0]
            source= data[1]
            des= data[2]
            moveBoxes(how_many, source, des)

        part1 = getTop()
        print('part1',part1)
        
        fillStacks()
        for line in lines:
            data = line.strip().split(sep=',')
            how_many=data[0]
            source= data[1]
            des= data[2]
            moveBoxes2(how_many, source, des)
        
    return getTop()

 
def moveBoxes(cnt, source, des):
    for i in range(0, int(cnt)):
        getStack(des).append(getStack(source).pop())

def moveBoxes2(cnt, source, des):
    temp_stack=[]
    for i in range(0, int(cnt)):
        temp_stack.append(getStack(source).pop())

    for i in range(0, int(cnt)):
        val = temp_stack.pop()
        getStack(des).append(val)


def getStack(val):
    if val == '1':
        return stack1
    elif val == '2':
        return stack2
    elif val == '3':
        return stack3
    elif val == '4':
        return stack4
    elif val == '5':
        return stack5
    elif val == '6':
        return stack6
    elif val == '7':
        return stack7
    elif val == '8':
        return stack8
    elif val == '9':
        return stack9
    else:
        raise Exception   

def getTop():
    val = stack1.pop() + stack2.pop() + stack3.pop() + stack4.pop() +stack5.pop() + stack6.pop() + stack7.pop() + stack8.pop() + stack9.pop() 
    return val


if __name__ == '__main__':
    print("day 5 result")
    print(day5())