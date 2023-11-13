# Write your solution here
from datetime import datetime

def is_it_valid(pic: str):
    result = True

    if len(pic) != 11:
        result = False

    if pic[6] not in 'A+-':
        result = False

    try:
        day = int(pic[0:2])
        month = int(pic[2:4])
        if pic[6] == 'A':
            year = int('20' + pic[4:6])
        elif pic[6] == '+':
            year = int('18' + pic[4:6])
        elif pic[6] == '-':
            year = int('19' + pic[4:6])

        born = datetime(year, month, day)
    except:
        result = False
    
    big_num = int(pic[0:6])*1000 + int(pic[7:10])
    
    string = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    
    control = string[big_num % 31]
    
    if control != pic[10]:
        result = False

    return result

