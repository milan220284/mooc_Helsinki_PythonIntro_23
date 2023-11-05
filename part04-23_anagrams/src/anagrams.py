# Write your solution here
def anagrams(first_word: str, second_word: str):
    
    if len(first_word) != len(second_word):
        return False

    word1 = sorted(first_word)
    word2 = sorted(second_word)

    for i in range(len(first_word)-1):
        if word1[i] != word2[i]:
            return False
    
    return True


if __name__ == "__main__":
    word1 = "lme"
    word2 = "mle1"

    print(anagrams(word1,word2))