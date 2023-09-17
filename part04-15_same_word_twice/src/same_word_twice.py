# Write your solution here
mylist = []

while True:
    word = input("Word: ")
    if word in mylist:
        print(f"You typed in {len(mylist)} different words")
        break

    mylist.append(word)
