# Write your solution here

mylist = []

while True:
    new = int(input("New item: "))
    
    if new == 0:
        break

    mylist.append(new)
    print("The list now:", mylist)
    print("The list in order:", sorted(mylist))

print("Bye!")