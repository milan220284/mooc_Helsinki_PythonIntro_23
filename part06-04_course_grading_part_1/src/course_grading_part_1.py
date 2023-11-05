# write your solution here



student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

students = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        students[int(parts[0])] = parts[1].strip() + ' '+ parts[2].strip()

grades = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        exercise_list = []
        for el in parts[1:]:
            exercise_list.append(int(el.strip()))
        grades[int(parts[0])] = exercise_list
    

for id, student in students.items():
    sum = 0
    if id in grades:
        for el in grades[id]:
            sum += el
    print(student + f' {sum}')