# Write your solution here

def spell(number):
    digit = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
        }

    decade = {
        2: "twenty",
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'
        }

    second_decade = {
        10: "ten",
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'
        }

    if number >= 0 and number < 10:
        return digit[number]
    elif number < 20:
        return second_decade[number]
    elif number < 100:
        if number % 10 != 0:
            return f"{decade[number//10]}-{digit[number%10]}"
        else:
            return f"{decade[number//10]}"
        


def dict_of_numbers():
    dictionary = {}
    for number in range(100):
        dictionary[number] = spell(number)
    return dictionary    

