directories = {'/':0}
path = '/'

def day7():
    with open('aoc2022/day7/input') as f:
        lines = f.readlines()
        for line in lines:
            processCMD(line)

    total = 0
    size2remove = 30000000 - (70000000 - directories['/'])
    possible_directories = []

    for directory in directories:
        if directories[directory] < 100000:
            total += directories[directory]

        if size2remove <= directories[directory]:
            possible_directories.append(directories[directory])


        
    return total, min(possible_directories)
def processCMD(cmd):
    global path
    if cmd[0] == '$':
        if cmd[2:4] == 'ls':
            pass # need later?
        elif cmd[2:4] == 'cd':
            if cmd[5:6] == '/':
                path = '/'
            elif cmd[5:7] == '..':
                path = path[0:path.rfind('/')]
            else: 
                directory_name = cmd.split()[2]
                print(directory_name)
                path = path + '/' + directory_name
                directories[path] = 0
    elif cmd[0:3] == 'dir':
        pass # mau need later
    else: #file size
        file_info = cmd.split()
        directory = path
        for i in range(path.count('/')):
            directories[directory] += int(file_info[0])
            directory= directory[:directory.rfind('/')]


if __name__ == '__main__':
    print("day 7 result")
    print(day7())