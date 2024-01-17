# WRITE YOUR SOLUTION HERE:
<<<<<<< HEAD
=======
class Car:
    def __init__(self) -> None:
        self.__petrol = 0
        self.__reading = 0

    def fill_up(self):
        self.__petrol = 60

    def drive(self, km:int):
        if km < self.__petrol:
            tmp = km
        else:
            tmp = self.__petrol
        self.__petrol -= tmp
        self.__reading += tmp

    def __str__(self):
        return f"Car: odometer reading {self.__reading} km, petrol remaining {self.__petrol} litres"
    
>>>>>>> a9d893b (finished part 9)
