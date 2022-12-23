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

    part1(forest, vis)
    #print(vis)
    #print(forest)

def part1(arr, visibility):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            visibility[i][j] = compare_edge(j, i, arr)

    cnt = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if visibility[i][j] == True:
                cnt +=1

    print(cnt)
            
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
    print(day8())