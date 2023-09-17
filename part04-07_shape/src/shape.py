# Copy here code of line function from previous exercise and use it in your solution
def line(n, string):
    if string == "":
        string = "*"
        
    print(n*string[0])

def box_of_hashes(height, width, char):
    # You should call function line here with proper parameters
    while height > 0:    
        line(width, char)
        height -= 1


def triangle(size, char):
    # You should call function line here with proper parameters
    tmp = 1
    while tmp <= size:
        line(tmp, char)
        tmp += 1


def shape(a, char1, b, char2):
    triangle(a, char1)
    box_of_hashes(b,a, char2)

# You can test your function by calling it within the following block

if __name__ == "__main__":
    shape(5, "x", 2, "o")