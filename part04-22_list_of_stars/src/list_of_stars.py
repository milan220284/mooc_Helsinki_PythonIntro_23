# Write your solution here

def list_of_stars(list):
    for el in list:
        print("*"*el)

if __name__ == "__main__":
    list = [1,3,5,2]
    list_of_stars(list)