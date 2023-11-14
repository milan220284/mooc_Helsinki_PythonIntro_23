# Write your solution here
import urllib.request

def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    database = my_request.read()
    active = []



    print(database[0])



retrieve_all()