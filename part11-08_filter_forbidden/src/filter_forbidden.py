# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    return "".join([char for char in list(string) if char not in list(forbidden)])

