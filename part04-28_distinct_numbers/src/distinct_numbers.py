# Write your solution here


def distinct_numbers(my_list):
    new_list = []
    for i in my_list:
        if i in new_list:
            pass
        else:
            new_list.append(i)
    new_list.sort()   
    return new_list
