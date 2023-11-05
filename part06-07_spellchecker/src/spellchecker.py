# write your solution here

words = []

with open("wordlist.txt") as new_file:
    for line in new_file:
        words.append(line.strip())

sentence = input("Write text: ")

sentence_list = sentence.split()


for word in sentence_list:
    if word.lower() not in words:
        word = '*'+word+'*'
    print(word +' ', end='')


