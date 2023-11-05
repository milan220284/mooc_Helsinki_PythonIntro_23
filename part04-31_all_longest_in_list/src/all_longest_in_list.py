# Write your solution here


def all_the_longest(my_list):
    if len(my_list) > 0:
        longest = len(my_list[1])
    else: 
        longest = None

    for i in my_list:
        if len(i) > longest:
            longest = len(i)

    new_list = []

    for i in my_list:
        if len(i) == longest:
            new_list.append(i)

    return new_list