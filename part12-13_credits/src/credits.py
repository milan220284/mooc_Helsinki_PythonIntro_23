from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def sum_of_all_credits(attempts: list):
    return reduce(lambda sum, student: sum + student.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    tmp = list(filter(lambda s: s.grade > 0, attempts))
    return reduce(lambda sum, student: sum + student.credits, tmp, 0)

def average(attempts: list):
    tmp = list(filter(lambda s: s.grade > 0, attempts))
    length = len(list(tmp))
    return reduce(lambda sum, student: sum + student.grade/length, tmp, 0)
