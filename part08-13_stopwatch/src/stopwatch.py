# Write your solution here:
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0
    
    def tick(self):
        seconds = self.seconds + 1
        self.seconds = seconds % 60
        self.minutes = (self.minutes + seconds//60) % 60
    
    def __str__(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"

