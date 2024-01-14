# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self) -> None:
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)

    def is_empty(self):
        if self.persons == []:
            return True
        else:
            return False
        
    def print_contents(self):
        for person in self.persons:
            print(person.name + f" ({person.height} cm)")

    def shortest(self):
        if len(self.persons) == 0:
            return None
        else:
            shortest = self.persons[0]
            for person in self.persons:
                if person.height < shortest.height:
                    shortest = person
            return shortest
        
    def remove_shortest(self):
        if len(self.persons) == 0:
            return None
        else:
            shortest = self.shortest()
            self.persons.remove(shortest)
            return shortest
