# Write your solution here
def older_people(people: list, year: int):
    output =[]
    for person in people:
        if person[1] < year:
            output.append(person[0])
    return output 
