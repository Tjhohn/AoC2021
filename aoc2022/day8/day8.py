import copy

def day8():
    forest = []
    vis = []
    with open('aoc2022/day8/input') as f:
        lines = f.readlines()
        for line in lines:
            row = []
            v = []
            for c in line.strip():
                row.append(c)
                v.append(False)


            forest.append(row)
            vis.append(v)

    part1(copy.deepcopy(forest), copy.deepcopy(vis))
    part2(copy.deepcopy(forest))

def part1(arr, visibility):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            visibility[i][j] = compare_edge(j, i, arr)

    cnt = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if visibility[i][j] == True:
                cnt +=1

    print('part 1 :', cnt)

def part2(arr):
    max_score = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            score = get_scenic_score(j, i, arr)
            if score > max_score:
                max_score = score

    print('part 2 :', max_score)
            
def get_scenic_score(x, y, trees): #ans too low..
    top, left, right, bottom = 0,0,0,0

    cur_cnt = 0
    for i in range(x-1, -1, -1):
        if int(trees[y][i]) < int(trees[y][x]):
            cur_cnt +=1
        elif int(trees[y][i]) >= int(trees[y][x]):
            cur_cnt +=1
            break
        else:
            break

    if cur_cnt > left:
        left = cur_cnt

    cur_cnt = 0
    for i in range(x+1, 99):
        if int(trees[y][i]) < int(trees[y][x]):
            cur_cnt += 1
        elif int(trees[y][i]) >= int(trees[y][x]):
            cur_cnt += 1
            break
        else:
            break

    if cur_cnt > right:
        right = cur_cnt
    
    cur_cnt = 0
    for i in range(y-1, -1, -1):
        if int(trees[i][x]) < int(trees[y][x]):
            cur_cnt += 1
        elif int(trees[i][x]) >= int(trees[y][x]):
            cur_cnt += 1
            break
        else:
            break
    
    if cur_cnt > top:
        top = cur_cnt

    cur_cnt = 0
    for i in range(y+1, 99):
        if int(trees[i][x]) < int(trees[y][x]):
            cur_cnt +=1
        elif int(trees[i][x]) >= int(trees[y][x]):
            cur_cnt +=1
            break
        else:
            break
    
    if cur_cnt > bottom:
        bottom =cur_cnt

    return left * right * top * bottom

def compare_edge(x, y, trees):
    if x == 0 or x == 98:
        return True
    
    if y == 0 or y == 98:
        return True

    cur_max = 0
    for i in range(0, x):
        if int(trees[y][i]) > int(cur_max):
            cur_max = trees[y][i]

    if int(cur_max) < int(trees[y][x]):
        return True

    cur_max = 0
    for i in range(x+1, 99):
        if int(trees[y][i]) > int(cur_max):
            cur_max = trees[y][i]

    if int(cur_max) < int(trees[y][x]):
        return True
    
    cur_max = 0
    for i in range(0, y):
        if int(trees[i][x]) > int(cur_max):
            cur_max = trees[i][x]
    
    if int(cur_max) < int(trees[y][x]):
        return True

    cur_max = 0
    for i in range(y+1, 99):
        if int(trees[i][x]) > int(cur_max):
            cur_max = trees[i][x]
    
    if int(cur_max) < int(trees[y][x]):
        return True

    return False
    
    
if __name__ == '__main__':
    print("day 8 result")
    day8()