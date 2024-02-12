import math 

def is_prime(x: int):
    for n in range(2, int(math.sqrt(x))+1):
        if x % n == 0 and x != n:
            return False
    return True

def prime_numbers():
    number = 2
    while True:
        if is_prime(number):
            yield number
        number += 1
