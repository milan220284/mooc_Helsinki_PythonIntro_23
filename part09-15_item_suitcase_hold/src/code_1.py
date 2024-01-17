# Write your solution here:
<<<<<<< HEAD
=======
class Item:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight

    def __str__(self):
        return self.__name + f" ({self.__weight} kg)"


class Suitcase:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
    
    def add_item(self, item):
        if item.weight() + self.weight() < self.capacity:
            self.items.append(item)
    
    def __str__(self):
        total_weight = 0
        for item in self.items:
            total_weight += item.weight()
        if len(self.items) == 1:
            string = "item"
        else:
            string = "items"
        return str(len(self.items)) + f" {string} ({total_weight} kg)"
    
    def print_items(self):
        for item in self.items:
            print(item)

    def weight(self):
        total_weight = 0
        for item in self.items:
            total_weight += item.weight()
        return total_weight
    
    def heaviest_item(self):
        if len(self.items) == 0:
            return None
        else:
            heaviest = self.items[0]
            for item in self.items:
                if item.weight() > heaviest.weight():
                    heaviest = item
            return heaviest
        
class CargoHold:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.suitcases = []

    def add_suitcase(self, suitcase):
        if suitcase.weight() + self.weight() < self.max_weight:
            self.suitcases.append(suitcase)

    def weight(self):
        total_weight = 0
        for item in self.suitcases:
            total_weight += item.weight()
        return total_weight
    
    def __str__(self):
        total_weight = 0
        for item in self.suitcases:
            total_weight += item.weight()
        if len(self.suitcases) == 1:
            string = "suitcase"
        else:
            string = "suitcases"
        return str(len(self.suitcases)) + f" {string}, space for {self.max_weight - total_weight} kg"        

    def print_items(self):
        for suitcase in self.suitcases:
            for item in suitcase.items:
                print(item)

>>>>>>> a9d893b (finished part 9)
