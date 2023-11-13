# Write your solution here
import string
from random import randint, shuffle

def generate_strong_password(length: int, number: bool, special_char: bool):
    password_list = []
    random = randint(0,25)
    password_list.append(string.ascii_lowercase[random])
    allowed_chars = string.ascii_lowercase
    if number:
        random = randint(0,8)
        password_list.append(string.digits[random])
        allowed_chars += string.digits
    
    special = '!?=+-()#'
    if special_char:
        random = randint(0,len(special)-1)
        password_list.append(special[random])
        allowed_chars += special
    
    for i in range(length - len(password_list)):
        random = randint(0,len(allowed_chars)-1)
        password_list.append(allowed_chars[random])
    shuffle(password_list)
    password = ''

    for el in password_list:
        password += el

    return password