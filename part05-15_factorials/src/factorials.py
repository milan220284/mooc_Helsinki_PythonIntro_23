# Write your solution here

def factorials(n: int):
    dict = {}
    dict[1] = 1
    for i in range(1, n):
        dict[i+1] = (i+1)*dict[i]
    return dict
