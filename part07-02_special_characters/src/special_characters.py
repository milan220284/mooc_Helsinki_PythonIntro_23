# Write your solution here

import string

def separate_characters(my_string: str):
    characters = list(my_string)
    ascii_characters = ''
    punctuation_characters = ''
    other_characters = ''
    for char in characters:
        if char in string.ascii_letters:
            ascii_characters += char
        elif char in string.punctuation:
            punctuation_characters += char
        else:
            other_characters += char 
    return ascii_characters, punctuation_characters, other_characters

    
