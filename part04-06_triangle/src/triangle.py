# Copy here code of line function from previous exercise
def line(n, string):
    if string == "":
        string = "*"
        
    print(n*string[0])

def triangle(size):
    # You should call function line here with proper parameters
    tmp = 1
    while tmp <= size:
        line(tmp, "#")
        tmp += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
