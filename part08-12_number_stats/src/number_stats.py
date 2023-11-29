# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        if len(self.numbers)>0:
            return sum(self.numbers)
        else:
            return 0

    def average(self):
        if len(self.numbers)>0:
            return self.get_sum()/self.count_numbers()
        else:
            return 0

print("Please type in integer numbers:")
new_stats = NumberStats()
even_stats = NumberStats()
odd_stats = NumberStats()

while True:
    number = int(input())
    if number == -1:
        break
    new_stats.add_number(number)
    if number % 2 == 0:
        even_stats.add_number(number)
    else:
        odd_stats.add_number(number)

print("Sum of numbers: " + str(new_stats.get_sum()))
print("Mean of numbers: " + str(new_stats.average()))
print("Sum of even numbers: " + str(even_stats.get_sum()))
print("Sum of odd numbers: " + str(odd_stats.get_sum()))