########################################################################
##
## CS 101
## Program #13
## Joe Epperson, IV
## jee4cf@umsystem.edu
##
## PROBLEM : A program designed to continuously pass time based upon an inputted time from the user
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
import time

class Clock:
    def __init__(self, hours = 0, minutes = 0, seconds = 0, types = 0):
        self.hours = int(hours)
        self.minutes = int(minutes)
        self.seconds = int(seconds)
        self.types = int(types)

    def tick(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.minutes += 1
            self.seconds -= 60
        else:
            self.seconds = self.seconds
        if self.minutes >= 60:
            self.hours += 1
            self.minutes -= 60
        else:
            self.minutes = self.minutes

    def __str__(self):
        if self.types == 0:
            if self.hours >= 24:
                self.hours -= 24
            return "{:02}:{:02}:{:02}".format(self.hours % 12, self.minutes, self.seconds)
        elif self.types == 1:
            if self.hours < 12:
                return "{:02}:{:02}:{:02} am".format(self.hours % 12, self.minutes, self.seconds)
            elif self.hours >=12 and self.hours <=24:
                return "{:02}:{:02}:{:02} pm".format(self.hours % 12, self.minutes, self.seconds)
            

hour = int(input("What is the current hour: "))
minute = int(input("What is the current minute: "))
second = int(input("What is the current second: "))
time1 = Clock(hour,minute,second)

#preventing an infinite loop
t = 0
while True:
    if t <=100:
        time1.tick()
        print(time1)
        time.sleep(1)
        t += 1
    else:
        break
