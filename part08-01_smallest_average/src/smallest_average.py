# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    average = [0]*3

    for i in range(1,4):
        average[0] += person1['result'+str(i)]
        average[1] += person2['result'+str(i)]
        average[2] += person3['result'+str(i)]
    
    for el in average:
        el = el/3

    min_av = average[0]
    index = 0
    i = 0
    print(average)

    for el in average:
        
        if el < min_av:
            min_av = el
            index = i
        i += 1

    print(index)

    if index == 0:
        return person1
    elif index == 1:
        return person2
    else:
        return person3
    