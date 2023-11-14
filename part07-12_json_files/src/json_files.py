# Write your solution here
import json

def print_persons(filename: str):
    with open(filename) as my_file:
        data = my_file.read()

    database = json.loads(data)

    for person in database:
        hobbies = '('
        for hoby in person["hobbies"]:
            hobbies += hoby
            hobbies += ', '
        if len(person['hobbies']) > 0:
            hobbies = hobbies[:-2] + ')'
        else:
            hobbies = '()'
        
        print(person['name'] +' '+ str(person['age']) + ' years ' +hobbies)

