from random import shuffle

def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper))
    shuffle(number_pool)
    weekly_draw = number_pool[0:amount]
    weekly_draw.sort()
    return weekly_draw
