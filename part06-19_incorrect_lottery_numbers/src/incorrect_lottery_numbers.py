# Write your solution here

def filter_incorrect():
    lines = []
    with open("lottery_numbers.csv") as new_file:
        for line in new_file:
            
            split = line.split(';')
            numbers = split[1].split(',')

            new_line = []
            new_line.append(split[0])
            for el in numbers:
                new_line.append(el.strip())
            lines.append(new_line)
    
    correct = []

    for line in lines:
        week = line[0].split(' ')

        try: 
            week_numb = int(week[1])
        except:
            continue

        if len(line) < 8:
            continue

        check = True


        for i in range(1,8):
            try:
                n = int(line[i])
            except:
                check = False

            if n > 39 or n < 0:
                check = False
            
            for j in range(1,8):
                if line[i] == line[j] and i != j:
                    check = False

        if check == True:
            correct.append(line)
    
    with open("correct_numbers.csv", 'w') as new_file:
        for line in correct:
            print(line)            
            string = line[0] + ';'
            for el in line[1:]:
                string = string + el + ','
            string = string[:-1] + '\n'
            new_file.write(string)

