# Write your solution here
from difflib import get_close_matches

words = []

with open("wordlist.txt") as new_file:
    for line in new_file:
        words.append(line.strip())

sentence = input("Write text: ")

sentence_list = sentence.split()
misspelled = []

for word in sentence_list:
    if word.lower() not in words:
        misspelled.append(word)
        word = '*'+word+'*'
    print(word +' ', end='')
print()
print("suggestions:")
for word in misspelled:
    suggestions = get_close_matches(word, words)
    print(word+":", end=" ")
    n = len(suggestions)
    count = 0
    for replacement in suggestions:
        count += 1
        print(replacement, end="")
        if count != n:
            print(", ", end="")
    print("")
    
