# Write your solution here

def length_of_longest(my_list):
    if len(my_list) > 0:
        longest = len(my_list[1])
    else: 
        longest = 0

    for i in my_list:
        if len(i) > longest:
            longest = len(i)

    return longest