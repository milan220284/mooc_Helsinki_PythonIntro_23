# WRITE YOUR SOLUTION HERE:
def recursive_sum(number: int):
    if number == 1:
        return 1
    return recursive_sum(number-1)+number