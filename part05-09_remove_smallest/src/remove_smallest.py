# Write your solution here

def remove_smallest(numbers: list):
    if len(numbers)>0:
        smallest = numbers[0]
    for item in numbers:
        if item < smallest:
            smallest = item
    numbers.remove(smallest)