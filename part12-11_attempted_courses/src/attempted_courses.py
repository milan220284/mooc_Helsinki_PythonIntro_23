class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def names_of_students(attempts: list):
    return list(map(lambda s: s.student_name, attempts))

def course_names(attempts: list):
    tmp = list(map(lambda s: s.course_name, attempts))
    return list(set(tmp))

