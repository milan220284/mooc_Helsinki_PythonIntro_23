# Write your solution here

while True:
    print('1 - add an entry, 2 - read entries, 0 - quit')
    option = int(input("Function: "))
    if option == 0:
        print("Bye now!\n")
        break

    print("Entries:")

    with open("diary.txt") as new_file:
        for line in new_file:
            print(line.strip())
    
    if option == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as my_file:
            my_file.write(entry+'\n')
        print("Diary saved\n")