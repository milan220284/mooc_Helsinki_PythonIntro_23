# Write your solution 
while True :
    string = input("Editor: ")

    if "viual studio code" == string.lower():
        print("an excellent choice!")
        break
    elif "word" == string.lower() or "notepad" == string.lower():
        print("awful")
    else :
        print("not good")
    