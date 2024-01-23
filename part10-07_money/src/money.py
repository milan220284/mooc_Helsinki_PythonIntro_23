# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        if self.__cents < 10:
            cents = "0"+str(self.__cents)
        else:
            cents = self.__cents
        return f"{self.__euros}.{cents} eur"

    def __eq__(self, another) -> bool:
        if self.__euros == another.__euros:
            if self.__cents == another.__cents:
                return True
        return False
    
    def __lt__(self, another) -> bool:
        if self.__euros*100+self.__cents < another.__euros*100+another.__cents:
            return True
        else:
            return False  
        
    def __gt__(self, another) -> bool:
        if self.__euros*100+self.__cents > another.__euros*100+another.__cents:
            return True
        else:
            return False 
    
    def __ne__(self, another) -> bool:
        if self.__euros*100+self.__cents != another.__euros*100+another.__cents:
            return True
        else:
            return False 
        
    def __add__(self, another):
        tmp = self.__euros*100 + another.__euros*100 + self.__cents + another.__cents
        euros = tmp//100
        cents = tmp - euros*100
        return Money(euros, cents)
    
    def __sub__(self, another):
        tmp = self.__euros*100 - another.__euros*100 + self.__cents - another.__cents
        if tmp < 0:
            raise ValueError("negative money")
        euros = tmp//100
        cents = tmp - euros*100
        return Money(euros, cents)
 