def day2():
    score = 0
    score2 =0 
    with open('aoc2022/day2/input') as f:
        lines = f.readlines()
        for line in lines:
            moves = line.split()
            score += gameResult(moves[0], moves[1])
            score2 += gameResult2(moves[0], moves[1])

    return score, score2
        

def gameResult(opp, you):
    score = 0
    if you == 'X':# rock
        score += 1
        if opp == 'A':
            score += 3
        elif opp == 'C':
            score += 6
    elif you =='Y':# paper
        score += 2
        if opp == 'B':
            score += 3
        elif opp == 'A':
            score += 6
    elif you == 'Z':#scissors
        score += 3
        if opp == 'C':
            score += 3
        elif opp == 'B':
            score += 6
    
    return score
    
def gameResult2(opp, you):
    if you == 'X':# lose
        if opp == 'A':
            return gameResult(opp, 'Z')  
        elif opp == 'B':
            return gameResult(opp, 'X')
        elif opp == 'C':
            return gameResult(opp, 'Y')
    elif you =='Y':# draw
        if opp == 'A':
            return gameResult(opp, 'X')  
        elif opp == 'B':
            return gameResult(opp, 'Y')
        elif opp == 'C':
            return gameResult(opp, 'Z')
    elif you == 'Z':#win
        if opp == 'A':
            return gameResult(opp, 'Y')  
        elif opp == 'B':
            return gameResult(opp, 'Z')
        elif opp == 'C':
            return gameResult(opp, 'X')
    

if __name__ == '__main__':
    print("day 2 result")
    print(day2() )  