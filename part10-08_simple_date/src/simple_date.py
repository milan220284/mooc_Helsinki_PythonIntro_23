# WRITE YOUR SOLUTION HERE:

class SimpleDate:
    def __init__(self, day, month, year) -> None:
        self.day = day
        self.month = month
        self.year = year
    
    def __eq__(self, another) -> bool:
        if self.day == another.day and self.month == another.month and self.year == another.year:
            return True
        else:
            return False  
        
    def __lt__(self, another) -> bool:
        if self.year < another.year:
            return True
        elif self.year == another.year:
            if self.month < another.month:
                return True
            elif self.month == another.month:
                if self.day < another.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False   

    def __gt__(self, another) -> bool:
        if self.year > another.year:
            return True
        elif self.year == another.year:
            if self.month > another.month:
                return True
            elif self.month == another.month:
                if self.day > another.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False             
    
    def __ne__(self, another) -> bool:
        if self.__eq__(another):
            return False
        else:
            return True 
    
    def __add__(self, days) -> bool:
        tmp = self.year*12*30 + self.month*30 + self.day
        tmp_year = (tmp+days)//360
        tmp_month = (tmp+days - tmp_year*360)//30
        tmp_day = tmp+days - tmp_year*360 - tmp_month*30
        return SimpleDate(tmp_day, tmp_month, tmp_year)
        
    def __str__(self) -> str:
        return f"{self.day}.{self.month}.{self.year}"

    def __sub__(self, another) -> bool:
        return abs(another.year*360+another.month*30+another.day - self.year*360-self.month*30-self.day)

