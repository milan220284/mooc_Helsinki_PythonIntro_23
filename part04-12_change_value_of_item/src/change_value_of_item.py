# Write your solution here
mylist = [1,2,3,4,5]

while True:
    index = int(input("Index: "))
    if index == -1:
        break
    new_value = int(input("New value: "))
    mylist[index]=new_value
    print(mylist)

