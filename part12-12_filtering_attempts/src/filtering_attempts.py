class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"
    
    def __lt__(self, another):
        return self.student_name < another.student_name


def accepted(attempts: list):
    return list(filter(lambda s: s.grade >= 1, attempts))

def attempts_with_grade(attempts: list, grade: int):
    return list(filter(lambda s: s.grade == grade, attempts))

def passed_students(attempts: list, course: str):
    tmp = list(filter(lambda s: s.grade > 0 and s.course_name == course, attempts))
    return list(map(lambda s: s.student_name, sorted(tmp)))


