# Write your solution here

def add_student(dictionary: dict, name: str):
    dictionary[name] = {}


def add_course(dictionary: dict, name: str, course: tuple):    
    if course[0] in dictionary[name]:
        previous = dictionary[name][course[0]]
        if previous < course [1]:    
            dictionary[name][course[0]] = course[1]
    else:
        dictionary[name][course[0]] = course[1]


def print_student(dictionary: dict, name: str):
    if name not in dictionary:
        print(name + ": no such person in the database")
    elif len(dictionary[name]) == 0:
        print(name + ":\n no completed courses")
    else:
        avrg = 0
        completed = 0
        for course in dictionary[name]:
            if dictionary[name][course] != 0:
                completed += 1
        if completed != 0:
            print(name+': ')
            print(f' {completed} ' + 'completed courses:')
            for course in dictionary[name]:
                if dictionary[name][course] != 0:
                    print('  ' + course + f' {dictionary[name][course]}')
                    avrg += dictionary[name][course]
            print(' average grade ' + f'{avrg/completed}')
        else:
            print(name + ":\n no completed courses")


def courses_completed(dictionary: dict, student: str):    
    completed = 0
    for course in dictionary[student]:
        if dictionary[student][course] != 0:
            completed += 1
    return completed


def most_completed(dictionary: dict):
    most = 0
    for name in dictionary:
        completed = 0
        for course in dictionary[name]:
            if dictionary[name][course] != 0:
                completed += 1
        if completed > most:
            most = completed
            student = name
    return student, most

def average(dictionary: dict, student: str):    
    completed = courses_completed(dictionary, student)    
    avr = 0
    for course in dictionary[student]:
        avr += dictionary[student][course]     
    if completed !=0:
        return avr/completed
    else:
        return 0


def best_average(dictionary: dict):
    best = 0
    for name in dictionary:
        avr = average(dictionary, name)
        if avr > best:
            best = avr
            student = name
    return student, best


def summary(dictionary: dict):
    print('students ' + f'{len(dictionary)}')

    name, most = most_completed(dictionary)
    print('most courses completed ' + f'{most} {name}')

    name, best = best_average(dictionary)
    print('best average grade ' + f'{best} {name}')

    