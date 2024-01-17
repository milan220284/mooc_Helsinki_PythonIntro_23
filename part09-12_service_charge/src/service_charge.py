# WRITE YOUR SOLUTION HERE:

<<<<<<< HEAD
=======
class BankAccount:
    def __init__(self, owner: str, acc_number: str, balance: float):
        self.__owner = owner
        self.__acc_number = acc_number
        self.__balance = balance
    
    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount: float):
        self.__balance -= amount
        self.__service_charge()

    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        self.__balance = 0.99*self.__balance

    
>>>>>>> a9d893b (finished part 9)

