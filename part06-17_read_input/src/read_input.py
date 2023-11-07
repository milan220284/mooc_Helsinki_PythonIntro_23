# Write your solution here
def read_input(string: str, lower: int, upper: int):
    while True:
        try:
            n = input(string)
            n = int(n)
            if n < upper and n > lower:
                return n
            else:
                print(f"You must type in an integer between {lower} and {upper}")
        except ValueError:
            print(f"You must type in an integer between {lower} and {upper}")
