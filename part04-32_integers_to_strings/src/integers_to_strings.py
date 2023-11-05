# Write your solution here
def formatted(my_list):
    new_list = []
    for item in my_list:
        str = f'{item:.2f}'
        new_list.append(str)
    return new_list
