# Write your solution here

import fractions

def fractionate(amount: int):
    n = fractions.Fraction(1, amount)
    result = []
    for i in range(amount):
        result.append(n)
    return result


