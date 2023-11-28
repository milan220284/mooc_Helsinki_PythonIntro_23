# Write your solution here
# Remember the import statement
from datetime import date

def list_years(dates: list) :
    years = []
    for date_iter in dates:
        years.append(date_iter.year)
    years.sort()
    return years

