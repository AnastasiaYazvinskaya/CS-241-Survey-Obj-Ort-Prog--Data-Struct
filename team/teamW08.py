"""
Author: Anastasia Yazvinskaya, (Faud Torres), Lindsay Gardels, Christian Maciel
Class: CS 241 - 03 (Fall 2021)
Assignment: Team W08
"""

""" CORE REQUIREMENTS """
class Time:
    """ Initialization of hours, minutes and seconds as private"""
    def __init__(self):
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0
    
    """ Getter and Setter for hours """
    def get_hours(self):
        return self.__hours

    def set_hours(self, newValue):
        if newValue > 23:
           self.__hours = 23
        elif newValue < 0:
            self.__hours = 0
        else:
            self.__hours = newValue
    
    hours = property(get_hours, set_hours)
    
    """ Getter and Setter for minutes """
    def get_minutes(self):
        return self.__minutes

    def set_minutes(self, newValue):
        if newValue > 59:
           self.__minutes = 59
        elif newValue < 0:
            self.__minutes = 0
        else:
            self.__minutes = newValue

    minutes = property(get_minutes, set_minutes)
    
    """ Getter and Setter for seconds """
    def get_seconds(self):
        return self.__seconds
    
    def set_seconds(self, newValue):
        if newValue > 59:
           self.__seconds = 59
        elif newValue < 0:
            self.__seconds = 0
        else:
            self.__seconds = newValue

    seconds = property(get_seconds, set_seconds)

""" STRETCH CHALLENGES """
class TimeStretch:
    """ Initialization of hour_in_seconds as private"""
    def __init__(self):
        self.__hour_in_seconds = 0
    
    """ Getter and Setter for hours """
    def get_hours(self):
        self.__hours = self.__hour_in_seconds // 3600
        return self.__hours

    def set_hours(self, newValue):
        if newValue > 23:
           self.__hours = 23
        elif newValue < 0:
            self.__hours = 0
        else:
            self.__hours = newValue
        self.__hour_in_seconds += self.__hours * 3600

    hours = property(get_hours, set_hours)
    
    """ Getter and Setter for minutes """
    def get_minutes(self):
        self.__minutes = self.__hour_in_seconds % 3600 // 60
        return self.__minutes

    def set_minutes(self, newValue):
        if newValue > 59:
           self.__minutes = 59
        elif newValue < 0:
            self.__minutes = 0
        else:
            self.__minutes = newValue
        self.__hour_in_seconds += self.__minutes * 60

    minutes = property(get_minutes, set_minutes)
    
    """ Getter and Setter for seconds """
    def get_seconds(self):
        self.__seconds = self.__hour_in_seconds % 3600 % 60
        return self.__seconds
    
    def set_seconds(self, newValue):
        if newValue > 59:
           self.__seconds = 59
        elif newValue < 0:
            self.__seconds = 0
        else:
            self.__seconds = newValue
        self.__hour_in_seconds += self.__seconds

    seconds = property(get_seconds, set_seconds)

    """ Getter for hours that returns the hours in a format of 1-12"""
    @property
    def hours_simple(self):
        if self.__hours == 0 or self.__hours == 12:
            hours = 12
        else:
           hours = self.__hours % 12
        return hours

    """ Geeter for hours that returns either "AM" or "PM" depending on the value of the hours"""
    @property
    def period(self):
        if self.__hours < 12:
            period = "AM"
        else:
           period = "PM"
        return period

def main():
    """
    This is the main driver for the program. It calls functions
    to prompt the user and get the results. Finally, it displays
    the results of the program.
    """
    """ Creating a Time object"""
    # Core Requirements
    print("CORE REQUIREMENTS")
    timeObj_1 = Time()

    """ Time input  (hours, minutes, seconds)"""
    timeObj_1.hours = int(input("Hour: "))
    timeObj_1.minutes = int(input("Minute: "))
    timeObj_1.seconds = int(input("Second: "))

    """ Time output """
    print(f"""{timeObj_1.hours}:{timeObj_1.minutes}:{timeObj_1.seconds}""")
    
    # Stretch Challenges
    print("STRETCH CHALLENGES")
    timeObj_2 = TimeStretch()

    """ Time input  (hours, minutes, seconds)"""
    timeObj_2.hours = int(input("Hour: "))
    timeObj_2.minutes = int(input("Minute: "))
    timeObj_2.seconds = int(input("Second: "))

    """ Time output """
    print(f"""{timeObj_2.hours_simple} {timeObj_2.period} {timeObj_2.minutes}:{timeObj_2.seconds}\n""")

if __name__ == "__main__":
    main()