# Write your solution here
def spruce(n):
    print("a spruce!")
    tmp = 0
    while tmp < n:
        print((n-tmp-1)*" "+(2*tmp+1)*"*")
        tmp += 1
    print((n-2)*" ", "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)