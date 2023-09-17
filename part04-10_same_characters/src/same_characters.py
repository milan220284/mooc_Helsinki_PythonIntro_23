# Write your solution here
def same_chars(string, a, b):
    if a < len(string) and b < len(string):
        return string[a]==string[b]
    else :
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))