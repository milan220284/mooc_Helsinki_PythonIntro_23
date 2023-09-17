# Copy here code of line function from previous exercise
def line(n, string):
    if string == "":
        string = "*"
        
    print(n*string[0])

def square_of_hashes(size):
    # You should call function line here with proper parameters
    tmp = size
    while tmp > 0:
        line(size, "#")
        tmp -= 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
