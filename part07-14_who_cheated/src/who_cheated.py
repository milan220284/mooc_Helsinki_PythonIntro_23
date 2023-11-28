# Write your solution here
from datetime import timedelta


def cheaters():
    start_times = {}
    submissions = {}
    cheaters = []

    with open("start_times.csv") as new_file:
        for line in new_file:
            new_line = line.split(';')
            h = int(new_line[1].split(':')[0])
            m = int(new_line[1].split(':')[1])
            
            start_times[new_line[0]] = timedelta(hours=h,minutes=m)
    
    with open("submissions.csv") as new_file:
        for line in new_file:
            new_line = line.split(';')
            h = int(new_line[3].split(':')[0])
            m = int(new_line[3].split(':')[1])

            if new_line[0] not in submissions.keys():
                submissions[new_line[0]] = []
                submissions[new_line[0]].append(timedelta(hours=h,minutes=m))
                
            submissions[new_line[0]].append(timedelta(hours=h,minutes=m))
    
    for student in start_times.keys():
        for end_time in submissions[student]:
            if end_time - start_times[student] > timedelta(hours=3):
                if student not in cheaters:
                    cheaters.append(student)

    return cheaters

