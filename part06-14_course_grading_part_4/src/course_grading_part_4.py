# tee ratkaisu tänne

# tee ratkaisu tänne


def grade(student):
    pts = student[0] + student[1]//4
    if pts < 15:
        mark = 0
    elif pts < 18:
        mark = 1
    elif pts < 21:
        mark = 2
    elif pts < 24:
        mark = 3
    elif pts < 28:
        mark = 4
    else:
        mark = 5

    return mark


if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_points = input("Exam points: ")
    course_info = input("Course information: ")
else:
    # now this is the False branch, and is never executed
    student_info = "students2.csv"
    exercise_data = "exercises2.csv"
    exam_points = "exam_points2.csv"
    course_info = 'course2.txt'

students = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        students[int(parts[0])] = parts[1].strip() + ' '+ parts[2].strip()

exercises = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        exercise_list = []
        for el in parts[1:]:
            exercise_list.append(int(el.strip()))
        exercises[int(parts[0])] = exercise_list
    
exam = {}

with open(exam_points) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        exam_pt = 0
        for el in parts[1:]:
            exam_pt += int(el.strip())
        exam[int(parts[0])] = exam_pt
    


name = None
credits = None

with open(course_info) as my_file:
    lines = []
    for line in my_file:
        new_line = line.split(':')
        lines.append(new_line)
    
    name = lines[0][1].strip()
    credits = lines[1][1].strip()
        

with open("results.txt", "w") as my_file:
    pass
    
with open("results.csv", "w") as my_file:
    pass
    
headline = "name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade"

with open("results.txt", "a") as my_file:
    my_file.write(name + ', ' + credits + ' credits\n')
    my_file.write('='*(len(name)+len(credits)+10) + '\n')
    my_file.write(headline + '\n')

    for id, student in students.items():
        exercise_done = 0
        if id in exercises:
            for el in exercises[id]:
                exercise_done += el
        exam_points = 0
        if id in exam:
            exam_points = exam[id]
        mark = grade([exam_points, exercise_done])
        pts = exam_points + exercise_done//4
        new_line = f"{student:30}{exercise_done:<10}{exercise_done//4:<10}{exam_points:<10}{pts:<10}{mark:<10}"
        my_file.write(new_line + '\n')

with open("results.csv", "a") as my_file:
    for id, student in students.items():
        exercise_done = 0
        if id in exercises:
            for el in exercises[id]:
                exercise_done += el
        exam_points = 0
        if id in exam:
            exam_points = exam[id]
        mark = grade([exam_points, exercise_done])
        new_line = f"{id};{student};{mark}"
        my_file.write(new_line + '\n')




