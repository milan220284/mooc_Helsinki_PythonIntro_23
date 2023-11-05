# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(word: str):
    
    n = len(word)-1

    for i in range(n):
        if word[i] != word[n-i]:
            return False
    
    return True

while True:
    word = input("Please type in a palindrome: ")
    
    if palindromes(word):
        print(word + " is a palindrome!")
        break
    else :
        print("that wasn't a palindrome")
