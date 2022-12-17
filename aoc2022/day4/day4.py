def day4():
    sum = 0
    sum2 = 0
    with open('aoc2022/day4/input') as f:
        lines = f.readlines()
        for line in lines:
            elfs = line.strip().split(sep=',')
            sum += isContained(elfs[0].split(sep='-'), elfs[1].split(sep='-'))
            sum2 += isOverlap(elfs[0].split(sep='-'), elfs[1].split(sep='-'))


    return sum, sum2
 
def isContained(a, b):
    ans = 0
    if int(a[0]) <= int(b[0]):
        if int(a[1]) >= int(b[1]):
            ans = 1

    if int(b[0]) <= int(a[0]):
        if int(b[1]) >= int(a[1]):
            ans = 1
    
    return ans

def isOverlap(a, b):
    ans = 0
    if int(a[0]) <= int(b[0]):
        if int(b[0]) <= int(a[1]):
            ans = 1

    if int(b[0]) <= int(a[0]):
        if int(a[0]) <= int(b[1]):
            ans = 1
    
    return ans

if __name__ == '__main__':
    print("day 4 result")
    print(day4()) 