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
            hobbies += ','
        hobbies = hobbies[:-1] + ')' 
        print(f'{person['name']} {person['age']} years ' + hobbies )