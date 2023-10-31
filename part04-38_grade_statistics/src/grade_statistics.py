# Write your solution here

def grade(student):
    pts = student[0] + student[1]//10
    if pts < 15 or student[0] < 10:
        grade = 0
    elif pts < 18:
        grade = 1
    elif pts < 21:
        grade = 2
    elif pts < 24:
        grade = 3
    elif pts < 28:
        grade = 4
    elif pts < 31:
        grade = 5

    return grade
    

def pass_percentage(students):
    success = 0
    for student in students:
        if grade(student) > 0:
            success += 1
    
    return success/len(students)


def pts_average(students):
    sum = 0
    for student in students:
        sum +=student[0]+student[1]//10
    return sum/len(students)

def grade_distribution(students):
    grades_number = [0,0,0,0,0,0]
    for student in students:
        mark = grade(student)
        grades_number[mark] += 1
    return grades_number


def print_stats(students):
    print("Statistics:")
    pts_avr = pts_average(students)
    print(f"Points average: {pts_avr:.1f}")
    pass_pct = pass_percentage(students)*100
    print(f"Pass percentage: {pass_pct:.1f}")
    print("Grade distribution:")
    grades_dst = grade_distribution(students)
    for i in range(6):
        print(f"{5-i}: ", end="")
        print("*"*grades_dst[5-i]) 

# the "main function" using these functions
students = []

while True:
    numbers = input("Exam points and exercises completed: ").split()
    student = []
    if len(numbers) == 0:
        break
    else:
        x = int(numbers[0])
        y = int(numbers[1])
        student.append(x)
        student.append(y)
        students.append(student)

    
print_stats(students)