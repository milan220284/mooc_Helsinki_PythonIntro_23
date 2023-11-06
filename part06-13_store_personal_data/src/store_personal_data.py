# Write your solution here
def store_personal_data(person: tuple):

    with open("people.csv", "a") as my_file:
        new_line = person[0] + f';{person[1]};{person[2]}'
        my_file.write(new_line + '\n')
