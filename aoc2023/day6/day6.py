def part1(input):
    times = input[0].split(":")[1].strip().split(' ')
    times = [int(time) for time in times if time != '']
    distances = input[1].split(":")[1].strip().split(' ')
    distances = [int(d) for d in distances if d != '']
    ways2win = []
    for index, time in enumerate(times):
        record_dist = distances[index]
        win_count =0
        m4m = 0
        for i in range(time+1):
            dist = i * (time-i)
            if dist > record_dist:
                win_count +=1

        ways2win.append(win_count)
    result = 1
    for number in ways2win:
        result *= number
    print(f" part 1 : {result}")

def part2(input):
    time = input[0].split(":")[1].strip()
    time = time.replace(" ", "")
    time = int(time)
    distance = input[1].split(":")[1].strip()
    distance = distance.replace(" ", "")
    distance = int(distance)
    print(f" time : {time} distance: {distance}")

    win_count =0
    for i in range(time+1):
        dist = i * (time-i)
        if dist > distance:
            win_count +=1

    print(f" part2 : {win_count}")

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()
    with open('testinput') as f:
        testinput = f.readlines()
    part1(testinput)
    part1(lines)
    part2(testinput)
    part2(lines)
