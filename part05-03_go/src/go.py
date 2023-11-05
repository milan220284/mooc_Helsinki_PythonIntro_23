# Write your solution here

def who_won(game_board: list):
    count_1 = 0
    count_2 = 0
    for row in game_board:
        for el in row:
            if el == 1:
                count_1 += 1
            elif el == 2:
                count_2 += 1
    
    if count_2 > count_1 :
        return 2
    elif count_1 > count_2 :
        return 1
    else :
        return 0