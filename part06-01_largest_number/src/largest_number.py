# write your solution here

def largest():
    count = 0
    largest = None
    with open("numbers.txt") as new_file:        
        for line in new_file:
            if count == 0:
                largest = int(line)

            line = line.replace("\n", "")
            number = int(line)
            if number > largest:
                largest = number
            print(largest)
            count += 1
    return largest
