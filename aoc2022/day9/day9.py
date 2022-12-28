def day9():
    tail_visited = set()
    tail_visited.add((0,0))
    head = [0, 0] # x, y
    tail = [0, 0] # x, y 
    with open('aoc2022/day9/input') as f:
        lines = f.readlines()
        for line in lines:
            head, tail = Action(head, tail, tail_visited, line)

    print(len(tail_visited)) #133 is wrong, 331 too low
            

def Action(head, tail, set, input):
    direction, steps = input.split()
    steps = int(steps)
    match direction:
        case 'R':
            for i in range(0, steps):
                head[0] = head[0] +1
                if not checkTail(head, tail):
                    tail = updateTail(head, tail)
                    set.add((tail[0],tail[1]))
            
            print('R : head :', head, 'tail :', tail)
        case 'U':
            for i in range(0, steps ):
                head[1] = head[1] + 1
                if not checkTail(head, tail):
                    tail = updateTail(head, tail)
                    set.add((tail[0],tail[1]))

            print('U : head :', head, 'tail :', tail)
        case 'L': #fixme
            for i in range(0, steps ):
                head[0] = head[0] -1
                if not checkTail(head, tail):
                    tail = updateTail(head, tail)
                    set.add((tail[0],tail[1]))

            print('L : head :', head, 'tail :', tail)
        case 'D':
            for i in range(0, steps):
                head[1] = head[1] -1
                if not checkTail(head, tail):
                    tail = updateTail(head, tail)
                    set.add((tail[0],tail[1]))

            print('D : head :', head, 'tail :', tail)
            
    return head, tail


def checkTail(head, tail):
    safe_pos = {(tail[0]-1, tail[1]-1), (tail[0], tail[1]-1), (tail[0]+1, tail[1]-1),
                (tail[0]-1, tail[1]),   (tail[0], tail[1]),   (tail[0]+1, tail[1]),
                (tail[0]-1, tail[1]+1), (tail[0], tail[1]+1), (tail[0]+1, tail[1]+1)}

    return (head[0],head[1]) in safe_pos

def updateTail(head, tail): # [0,3] and [1,1] -> ret [0,2] not [0,1]
    diff_x = head[0] - tail[0]
    diff_y = head[1] - tail[1]
    if abs(diff_x) > 1 or abs(diff_y) > 1:
        return [tail[0] + sign(diff_x), tail[1] + sign(diff_y)]
    return tail

def sign( num : int ):
    if num < 0:
        return -1
    elif num == 0:
        return 0
    elif num > 0:
        return 1

if __name__ == '__main__':
    print("day 9 result")
    day9()
    print(updateTail([0,3], [1,1]))