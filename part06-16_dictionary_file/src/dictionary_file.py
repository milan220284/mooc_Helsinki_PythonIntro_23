# Write your solution here

dictionary = {}

with open("dictionary.txt") as new_file:
    for line in new_file:
        new_line = line.split(';')
        dictionary[new_line[0]] = new_line[1] 


while True:
    print('1 - Add word, 2 - Search, 3 - Quit')
    option = int(input("Function: "))
    if option == 3:
        print("Bye!\n")
        break

    if option == 1:
        finnish = input("The word in Finnish: ")
        english = input("The word in English: ")
        dictionary[finnish] = english
        with open("dictionary.txt", 'a') as new_file:
            new_file.write(finnish + ';' + english + '\n') 
        print("Dictionary entry added")
        
    if option == 2:
        search_term = input("Search term:  ")
        for key, value in dictionary.items():
            if search_term in key:
                print(key + " - " + value)
            if search_term in value:
                print(key + " - " + value)

