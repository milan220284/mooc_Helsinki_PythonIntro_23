# Write your solution here

def list_sum(list1, list2):
    new_list = []
    n = len(list1)
    for i in range(n):
        new_list.append(list1[i]+list2[i])   
    return new_list