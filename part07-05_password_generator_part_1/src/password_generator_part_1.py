# Write your solution here
import string
from random import randint

def generate_password(length: int):
    string.ascii_lowercase
    password = ''
    for i in range(length):
        random = randint(0,25)
        password += string.ascii_lowercase[random]
    return password
