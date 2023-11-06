# Write your solution here


def filter_solutions():
    lines = []

    with open("solutions.csv") as new_file:
        for line in new_file:
            new_line = line.split(';')
            lines.append(new_line)
    
    with open("correct.csv", "w") as my_file:
        pass
    
    with open("incorrect.csv", "w") as my_file:
        pass
    
    correct = []

    incorrect = []

    for line in lines:
        result = int(line[2])
        if '-' in line[1]:
            operands = line[1].split('-')
            if int(operands[0]) - int(operands[1]) == result:
                correct.append(line)
            else:
                incorrect.append(line)
        if '+' in line[1]:
            operands = line[1].split('+')
            if int(operands[0]) + int(operands[1]) == result:
                correct.append(line)
            else:
                incorrect.append(line)
    
    with open("correct.csv", "w") as my_file:
        for line in correct:
            new_line = f"{line[0]};{line[1]};{line[2]}"
            my_file.write(new_line)
    
    with open("incorrect.csv", "w") as my_file:
        for line in incorrect:
            new_line = f"{line[0]};{line[1]};{line[2]}"
            my_file.write(new_line)
    