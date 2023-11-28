# Write your solution here
import string

def change_case(orig_string: str):
    tmp = list(orig_string)
    new = ""
    for el in tmp:
        if el.islower():
            el = el.upper()
        elif el.isupper():
            el = el.lower()
        new += el
    return new
    
def split_in_half(orig_string: str):
    n = len(orig_string)
    return orig_string[:n//2], orig_string[n//2:]

def remove_special_characters(orig_string: str):
    tmp = list(orig_string)
    new = ""

    for el in tmp:
        if el in string.ascii_letters or el in string.digits or el == " ":
            new += el
    
    return new

    