# Write your solution here
import urllib.request
import json

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = my_request.read()
    active = []
    database = json.loads(data)
    for el in database:
        if el["enabled"]==True:
            tulpe = (el['fullName'],el['name'],el['year'],sum(el['exercises']))
            active.append(tulpe)
    
    return active

def retrieve_course(course_name: str):
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses/"+ course_name+"/stats")
    data = my_request.read()
    database = json.loads(data)
    if len(database) == 0:
        return None
    number_weeks = 0
    first = list(database.keys())[0]
    max_students = database[first]['students']
    hours = 0
    exercises = 0
    students = 0
    
    for el in database:
        number_weeks += 1
        students += database[f'{el}']['students']
        tmp = database[f'{el}']['students'] 
        if tmp > max_students:
            max_students = database[f'{el}']['students']
        hours += database[f'{el}']['hour_total']
        exercises += database[f'{el}']['exercise_total']
    
    exercises_average = round(exercises//max_students)
    hours_average = round(hours//max_students)

    result = {
        'weeks': number_weeks,
        'students': max_students,
        'hours': hours,
        'hours_average': hours_average,
        'exercises': exercises,
        'exercises_average': exercises_average
        }

    return result
