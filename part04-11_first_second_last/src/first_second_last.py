# Write your solution here
def first_word(sentence):
    return sentence[:sentence.find(" ")]

def second_word(sentence):
    index1 = sentence.find(" ")
    index2 = sentence[index1+1:].find(" ")
    if index2 > 0:
        return sentence[index1+1:index1+index2+1]
    else :
        return sentence[index1+1:]

def last_word(sentence):
    while len(sentence)>0:
        index = sentence.find(" ")
        if index > 0:
            sentence = sentence[index+1:]
        else :
            break
    return sentence

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))