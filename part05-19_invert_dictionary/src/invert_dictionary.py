# Write your solution here

def invert(dictionary):
    tmp = {}
    for key, value in dictionary.items():
        tmp[value] = key
    dictionary.clear()
    for key, value in tmp.items():
        dictionary[key] = value
   