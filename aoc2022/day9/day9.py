def day9part1():
    tail_visited = set()
    tail_visited.add((0,0))
    head = [0, 0] # x, y
    tail = [0, 0] # x, y 
    with open('aoc2022/day9/input') as f:
        lines = f.readlines()
        for line in lines:
            head, tail = Action_p1(head, tail, tail_visited, line)

    print(len(tail_visited))
    
def day9part2():
    tail_visited = set()
    tail_visited.add((0,0))
    knots = [[0,0]]*10 # x, y
    print(knots)
    with open('aoc2022/day9/input') as f:
        lines = f.readlines()
        for line in lines:
            knots = Action_p2(knots, tail_visited, line)

    print(len(tail_visited)) #761 too low
            

def Action_p2(knots, set, input):
    direction, steps = input.split()
    steps = int(steps)
    match direction:
        case 'R':
            for i in range(0, steps):
                knots[0] = (knots[0][0]+1, knots[0][1])
                for j in range(1, 10): #check and update each knot
                    if not checkTail(knots[j-1], knots[j]):
                        knots[j] = updateTail(knots[j-1], knots[j])
                        set.add((knots[-1][0],knots[-1][1]))
                        
            print('R : knots:', knots)
        case 'U':
            for i in range(0, steps ):
                knots[0] = (knots[0][0], knots[0][1]+1)
                for j in range(1, 10): #check and update each knot
                    if not checkTail(knots[j-1], knots[j]):
                        knots[j] = updateTail(knots[j-1], knots[j])
                        set.add((knots[-1][0],knots[-1][1]))

            print('U : knots:', knots)
        case 'L': 
            for i in range(0, steps ):
                knots[0] = (knots[0][0]-1, knots[0][1])
                for j in range(1, 10): #check and update each knot
                    if not checkTail(knots[j-1], knots[j]):
                        knots[j] = updateTail(knots[j-1], knots[j])
                        set.add((knots[-1][0],knots[-1][1]))

            print('L : knots:', knots)
        case 'D':
            for i in range(0, steps):
                knots[0] = (knots[0][0], knots[0][1]-1)
                for j in range(1, 10): #check and update each knot
                    if not checkTail(knots[j-1], knots[j]):
                        knots[j] = updateTail(knots[j-1], knots[j])
                        set.add((knots[-1][0],knots[-1][1]))

            print('D : knots:', knots)

    return knots

def Action_p1(head, tail, set, input):
    direction, steps = input.split()
    steps = int(steps)
    match direction:
        case 'R':
            for i in range(0, steps):
                head[0] = head[0] +1
                if not checkTail(head, tail):
                    tail = updateTail(head, tail)
                    set.add((tail[0],tail[1]))
            
            # print('R : head :', head, 'tail :', tail)
        case 'U':
            for i in range(0, steps ):
                head[1] = head[1] + 1
                if not checkTail(head, tail):
                    tail = updateTail(head, tail)
                    set.add((tail[0],tail[1]))

            # print('U : head :', head, 'tail :', tail)
        case 'L':
            for i in range(0, steps ):
                head[0] = head[0] -1
                if not checkTail(head, tail):
                    tail = updateTail(head, tail)
                    set.add((tail[0],tail[1]))

            # print('L : head :', head, 'tail :', tail)
        case 'D':
            for i in range(0, steps):
                head[1] = head[1] -1
                if not checkTail(head, tail):
                    tail = updateTail(head, tail)
                    set.add((tail[0],tail[1]))

            # print('D : head :', head, 'tail :', tail)

    return head, tail

def checkTail(head, tail):
    safe_pos = {(tail[0]-1, tail[1]-1), (tail[0], tail[1]-1), (tail[0]+1, tail[1]-1),
                (tail[0]-1, tail[1]),   (tail[0], tail[1]),   (tail[0]+1, tail[1]),
                (tail[0]-1, tail[1]+1), (tail[0], tail[1]+1), (tail[0]+1, tail[1]+1)}

    return (head[0],head[1]) in safe_pos

def updateTail(head, tail): 
    diff_x = (head[0] - tail[0])
    diff_y = (head[1] - tail[1])
    if abs(diff_x) > 1 or abs(diff_y) > 1:
        return [tail[0] + checkSign(diff_x), tail[1] + checkSign(diff_y)]
    return tail

def checkSign( num : int ):    
    if num < 0:
        return -1
    elif num == 0:
        return 0
    elif num > 0:
        return 1

if __name__ == '__main__':
    print("day 9 result")
    day9part1()
    day9part2()