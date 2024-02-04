# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

def count_subordinates(employee: Employee):
    if employee.subordinates == []:
        return 0
    count = 0
    for subordinate in employee.subordinates:
        count += count_subordinates(subordinate)
    return len(employee.subordinates) + count
