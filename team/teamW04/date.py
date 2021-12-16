""" CORE REQUIREMENTS """
class Date:
    def __init__(self, day=1, month=1, year=200):
        self.day = day
        self.month = month
        self.year = year

    def prompt(self):
        self.day = int(input("Enter a day: "))
        self.month = int(input("Enter a month: "))
        self.year = int(input("Enter a year: "))

    def display(self):
        print(f"{self.month}/{self.day}/{self.year}")

""" STRETCH CHALLENGES """
class DateStretch:
    def __init__(self, day=1, month=1, year=200):
        self.day = day
        self.month = month
        self.year = year

    """
    1. Detect if a user enters an invalid month (not 1-12) or a year before 2000 and reprompt them. (We won't worry about days at this point...)
    """
    def prompt(self):
        self.day = int(input("Enter a day: "))

        invalid = True
        while invalid:
            self.month = int(input("Enter a month: "))
            if self.month >= 1 and self.month <= 12:
                invalid = False
        
        invalid = True
        while invalid:
            self.year = int(input("Enter a year: "))
            if self.year >= 2000:
                invalid = False

    """
    2. Change the display function for dates so that months and days are always two digits (e.g. 01/02/2000 instead of 1/2/2000).
    """
    def display(self):
        print(f"{self.month:02d}/{self.day:02d}/{self.year}")
    """
    3. Create a display_long function for dates to display them in long format: January 01, 2000 (instead of 01/01/2000)
    """
    def display_long(self):
        if self.month == 1:
            month_name = "January"
        elif self.month == 2:
            month_name = "Fabruary"
        elif self.month == 3:
            month_name = "March"
        elif self.month == 4:
            month_name = "April"
        elif self.month == 5:
            month_name = "May"
        elif self.month == 6:
            month_name = "June"
        elif self.month == 7:
            month_name = "July"
        elif self.month == 8:
            month_name = "August"
        elif self.month == 9:
            month_name = "September"
        elif self.month == 10:
            month_name = "October"
        elif self.month == 11:
            month_name = "November"
        elif self.month == 12:
            month_name = "December"
        print(f"{month_name} {self.day}, {self.year}")