

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    test = []
    for i in range(5):
        test.append(i)

    print(test)
    test.pop()
    print(test)

    print(4 % 40)
    print(40 % 40)
    print(45 % 40)
    print(70 % 40)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
