# Write your solution here
from random import randint

def roll(die: str):
    die_A = '333336'
    die_B = '222555'
    die_C = '144444'
    choosen = None
    if die == 'A':
        choosen = die_A
    elif die == "B":
        choosen = die_B
    else:
        choosen = die_C
    
    rand = randint(0,5)
    return int(choosen[rand])

def play(die1: str, die2: str, times: int):
    wins_1 = 0
    wins_2 = 0
    i = 0
    while i < times:
        i += 1
        roll_1 = roll(die1)
        roll_2 = roll(die2)

        if roll_1 > roll_2:
            wins_1 += 1
        elif roll_2 > roll_1:
            wins_2 += 1
    return wins_1, wins_2, times - wins_1 - wins_2
