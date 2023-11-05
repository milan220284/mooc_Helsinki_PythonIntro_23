# Write your solution here
def most_common_character(string):
    max = 0
    for i in range(len(string)):
        iter = string.count(string[i])
        if iter > max:
            max = iter
            character = string[i]
    return character


