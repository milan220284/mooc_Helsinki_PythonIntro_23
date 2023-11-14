# Write your solution here
from random import shuffle

def words(n: int, beginning: str):
    words = []
    with open("words.txt") as new_file:
        for line in new_file:
            words.append(line.strip())

    words_prefix = []
    for el in words:
        if el.startswith(beginning):
            words_prefix.append(el)
    
    shuffle(words_prefix)

    if len(words_prefix) > n:
        result = words_prefix[0:n]
        return result
    else:
        raise ValueError    

    
