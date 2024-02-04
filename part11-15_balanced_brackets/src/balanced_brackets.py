def clean(my_string):
    if len(my_string) == 0:
        return ''
    if my_string[0] in ['(',')','[',']']:
        return my_string[0] + str(clean(my_string[1:]))
    return clean(my_string[1:])
    
def balanced_brackets(my_string: str):
    my_string = clean(my_string)
    if len(my_string) == 0:
        return True
    if not (my_string[0] == '(' and my_string[-1] == ')') and not (my_string[0] == '[' and my_string[-1] == ']'):
        return False
    

    # remove first and last character
    return balanced_brackets(my_string[1:-1])

