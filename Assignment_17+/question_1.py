class Clock:
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def str_update(self, time):
        self.hours, self.minutes, self.seconds = map(int, time.split(":"))

    def __str__(self) -> str:
        return f"{self.hours} hours, {self.minutes} minutes and {self.seconds} seconds"

    def add_clocks(self, other):
        second_overflow = (self.seconds + other.seconds) // 60
        minutes_overflow = (self.minutes + other.minutes + second_overflow) // 60
        
        seconds = (self.seconds + other.seconds) % 60
        minutes = (self.minutes + other.minutes + second_overflow) % 60
        hours = (self.hours + other.hours + minutes_overflow) % 24

        return Clock(hours, minutes, seconds)



clock1 = Clock()
clock2 = Clock()
clock1.str_update("20:10:52")
clock2.str_update("08:49:24")
print(clock1)
print(clock2)
clock3 = clock1.add_clocks(clock2)
print(clock3)
