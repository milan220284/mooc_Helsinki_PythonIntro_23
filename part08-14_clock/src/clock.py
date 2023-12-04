# Write your solution here:
# Write your solution here:
class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
    
    def tick(self):
        seconds = self.seconds + 1
        self.seconds = seconds % 60
        minutes = self.minutes + seconds//60
        self.minutes = minutes % 60
        self.hours = (minutes//60 + self.hours)%24
    
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def set(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0
