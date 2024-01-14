# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self) -> str:
        result = self.name + f" ({self.weight}kg)"
        return result
    
class Box:
    def __init__(self) -> None:
        self.presents = []
        
    def add_present(self, present: Present):
        self.presents.append(present)

    def total_weight(self):
        total = 0
        for present in self.presents:
            total += present.weight
        return total

