from collections import deque
import time


def day12():
    grid = []

    with open('aoc2022/day12/input') as f:
        lines = f.readlines()
        for line in lines:
            grid.append(line.strip())

    # make dictionary of heigths from char to int values
    height_map = {chr(i): i - 96 for i in range(97, 97+26)}
    height_map['S'] = 1
    height_map['E'] = 26
    # valid directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    Part1(grid, directions, height_map)
    Part2(grid, directions, height_map)

def Part1(grid, directions, height_map):
    start, end = None, None
    for i, line in enumerate(grid):
        if 'S' in line:
            j = line.index('S')
            start = (i, j)
        if 'E' in line:
            j = line.index('E')
            end = (i, j)
    # find start and end
    
    
    
    print(len(BFS(start, end, grid, directions, height_map)) -1 )
    return len(BFS(start, end, grid, directions, height_map)) -1
    # call BFS

def Part2(grid, directions, height_map):
    # find all a's and S and return one with shortest route
    starts = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'a':
                starts.append((i, j))

    end = None
    for i, line in enumerate(grid):
        if 'E' in line:
            j = line.index('E')
            end = (i, j)


    min_dist = Part1(grid, directions, height_map)
    for start in starts:
        distance = BFS(start, end, grid, directions, height_map)
        if distance is not None:
            min_dist = min(min_dist, len(distance)-1)
    
    print(min_dist)

def BFS(start, end, grid, directions, height_map):
    q = deque()
    seen = set()
    q.append([start])
    while q:
        path = q.popleft()
        r, c = path[-1]
        if (r, c) not in seen:
            seen.add((r, c))
            if (r, c) == end:
                return path
            ch = grid[r][c]
            height1 = height_map[ch]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    ch = grid[nr][nc]
                    height2 = height_map[ch]
                    if height2 <= height1 + 1:
                        path_copy = path[:]
                        path_copy.append((nr, nc))
                        q.append(path_copy)

def PrintGrid(grid):
    print('*' * 80)
    for line in grid:
        print('\t' + line + '\t')
    print('*' * 80)

if __name__ == '__main__':
    print("day 12 result")
    day12()