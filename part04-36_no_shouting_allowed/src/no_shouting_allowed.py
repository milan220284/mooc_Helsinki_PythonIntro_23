# Write your solution here

def no_shouting(my_list: list):
    new_list = []
    for i in my_list:
        if i.isupper():
            pass
        else:
            new_list.append(i)
    return new_list
