# Write your solution here

from datetime import datetime, timedelta, date

filename = input("Filename: ")
start_tmp = input("Starting date: ")
days = int(input("How many days: "))
start_tmp = start_tmp.split('.')
start = datetime(int(start_tmp[2]),int(start_tmp[1]),int(start_tmp[0]))
print("Please type in screen time in minutes on each day (TV computer mobile):")

summed = 0
date = start
file = []

for i in range(days):
    string = f"{date.date()}"
    date_list = string.split('-')
    input_tmp = input("Screen time " + date_list[2]+"."+date_list[1]+"."+date_list[0] + ": ")
    input_tmp = input_tmp.split(' ')
    summed += int(input_tmp[2])+int(input_tmp[1])+int(input_tmp[0])
    date = date + timedelta(days=1)
    file_input = date_list[2]+"."+date_list[1]+"."+date_list[0]+': '+input_tmp[0]+'/'+input_tmp[1]+'/'+input_tmp[2]
    file.append(file_input)

date = date + timedelta(days=-1)

string = f"{date.date()}"
date_list = string.split('-')
final = date_list[2]+"."+date_list[1]+"."+date_list[0]

string_start = f"{start.date()}"
start_list = string_start.split('-')
start_ = start_list[2]+"."+start_list[1]+"."+start_list[0]


with open(filename, "w") as my_file:
        new_line = "Time period: "+start_+"-"+final
        my_file.write(new_line + '\n')
        new_line = f"Total minutes: {summed}"
        my_file.write(new_line + '\n')
        new_line = f"Average minutes: {summed/days}"
        my_file.write(new_line + '\n')
        for line in file:
            my_file.write(line + '\n')





