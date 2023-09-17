# Copy here code of line function from previous exercise
def line(n, string):
    if string == "":
        string = "*"
        
    print(n*string[0])

def square(size, character):
    # You should call function line here with proper parameters
    tmp = size
    while tmp > 0:
        line(size, character)
        tmp -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")