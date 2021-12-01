

def depth_increases(filename):
    f = open(filename, "r")
    total_increases = 0
    received_start = False
    prev = 0
    for x in f:
        if received_start == False:
            prev = int(x)
            received_start = True
        else:
            if int(x) > prev:
                total_increases += 1
            prev = int(x)

    return total_increases

def depth_window(filename):
    f = open(filename, "r")
    total_increases = 0
    received_start = False
    prev = 0
    for x in f:
        if received_start == False:
            prev = int(x)
            received_start = True
        else:
            if int(x) > prev:
                total_increases += 1
            prev = int(x)

    return total_increases

if __name__ == '__main__':
    print(depth_increases('input.txt'))
