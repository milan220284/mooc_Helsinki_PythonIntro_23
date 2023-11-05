# Write your solution here

def shortest(my_list):
    if len(my_list) > 0:
        shortest = my_list[1]
    else: 
        shortest = None

    for i in my_list:
        if len(i) < len(shortest):
            shortest = i

    return shortest