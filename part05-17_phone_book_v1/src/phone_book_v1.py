# Write your solution here

book = {}

while True:
    option = int(input("command (1 search, 2 add, 3 quit): "))

    if option == 3:
        print("quitting...")
        break

    if option == 2:
        name = input("name: ")
        number = input("number: ")
        book[name] = number
        print("ok!")

    if option == 1:
        name = input("name: ")
        if name in book:
            print(f"{book[name]}")
        else:
            print("no number")



