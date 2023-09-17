# Write your solution here
list = []
print("The list is now", list)

while True:
    command = input("a(d)d, (r)emove or e(x)it: ")
    if command == "r":
        list.pop()
        print("The list is now", list)
    elif command == "d":
        if len(list) > 0:
            list.append(len(list)+1)
            print("The list is now", list)
        else :
            list.append(1)
            print("The list is now", list)
    else :
        break
print("Bye!")
    