
def day1():
    elves = {}
    elf_cnt=0
    max_cals = 0
    with open('input') as f:
        lines = f.readlines()
        for line in lines:
            if line != '\n':
                if elf_cnt in elves:
                    elves[elf_cnt] += int(line)
                else:
                    elves[elf_cnt] = int(line)

                if elves[elf_cnt] > elves[max_cals]:
                    max_cals = elf_cnt
            else:
                elf_cnt +=1 

    sort = dict(sorted(elves.items(), key=lambda item: item[1],  reverse=True))
    key_list = list(sort.keys())
    t3t = sort[key_list[0]] + sort[key_list[1]]+ sort[key_list[2]]        

    print(sort)

    return elves[max_cals], t3t


if __name__ == '__main__':
    print("day 1 result")
    print(day1() )  