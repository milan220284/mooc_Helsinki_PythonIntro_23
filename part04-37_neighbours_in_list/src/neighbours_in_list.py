# Write your solution here
def longest_series_of_neighbours(my_list):
    j=1
    max = j
    i=0
    while i < len(my_list)-1:
        if abs(my_list[i+1]-my_list[i]) == 1:
            i+=1
            j+=1
        else:
            i+=1
            if max < j:
                max=j
            j=1

    if max < j:
        max=j
    return max

