# WRITE YOUR SOLUTION HERE:
def begin_with_vowel(words: list):
    return [word for word in words if word.lower()[0] in ['a','e','i','o','u']]