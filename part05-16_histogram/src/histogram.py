# Write your solution here

def histogram(string):
    output = {}
    for i in range(len(string)):
        char = string[i]
        if char not in output:
            output[char] = 0
        output[char] += 1
    
    for key, value in output.items():
        print(f"{key} " + "*"*value)