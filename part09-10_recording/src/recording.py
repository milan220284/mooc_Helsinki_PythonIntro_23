# WRITE YOUR SOLUTION HERE:
<<<<<<< HEAD
=======

class Recording:
    def __init__(self, length):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("The length must not be below zero")

    # A getter method
    @property
    def length(self):
        return self.__length

    # A setter method
    @length.setter
    def length(self, length):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("The length must not be below zero")

>>>>>>> a9d893b (finished part 9)
