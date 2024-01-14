# Write your solution after the class Car
# Do not make changes to the class!
class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"

# WRITE YOUR SOLUTION HERE:

def fastest_car(cars: list):
    if len(cars) == 0:
        return None
    result = cars[0]
    top_speed = result.top_speed
    for car in cars:
        if car.top_speed > top_speed:
            result = car
            top_speed = car.top_speed
    return result.make

