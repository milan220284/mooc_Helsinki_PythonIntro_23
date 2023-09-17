def line(n, string):
    if string == "":
        string = "*"
        
    print(n*string[0])

if __name__ == "__main__":
    line(5, "x")