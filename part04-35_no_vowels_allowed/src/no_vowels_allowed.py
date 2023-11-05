# Write your solution here
def no_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o' ,'u']
    for vow in vowels:
        my_string = my_string.replace(vow, "")
    return my_string


