"""
Author: Anastasia Yazvinskaya, (Faud Torres), Lindsay Gardels, Christian Maciel
Class: CS 241 - 03 (Fall 2021)
Assignment: Team W03
"""

""" CORE REQUIREMENTS """
class Rational:
    """
    1. Have your class initialize the numerator to 0 and the denominator to 1 (Hint: Use the __init__ function). Then create a display member function (method) that displays the number in the format: "top/bottom", such as: "3/4" or "0/1". No need to reduce the fraction at this point.

    Have main create a new rational number and display it. Verify that your result looks correct.
    """
    def __init__(self, top=0, bottom=1):
        self.top = top
        self.bottom = bottom
    """
    2. Create a prompt member function (aka method) that prompts the user for the numerator and the denominator. Then change main so that it creates a new object, displays it, calls prompt, and displays it again.
    """
    def prompt(self):
        self.top = int(input("Enter the numenator: "))
        self.bottom = int(input("Enter the denominator: "))
    """
    3. Create an additional display method called display_decimal that displays the fraction in decimal form (e.g., 3/4 would display as 0.75). Then, add a line at the end of main to display the decimal version of your number in addition to the standard version.
    """
    def display_decimal(self):
        print(f"Decimal: {self.top/self.bottom:.2f}")

""" STRETCH CHALLENGES """
class RetionalStretch:
    def __init__(self, top=0, bottom=1):
        self.top = top
        self.bottom = bottom
    
    def prompt(self):
        self.top = int(input("Enter the numenator: "))
        self.bottom = int(input("Enter the denominator: "))
    """
    1. Change your display function so that if the value is an improper fraction (larger on top than bottom), it displays it as a mixed number, such as: "1 1/4", rather than "5/4".
    """
    def display_decimal(self):
        if self.top > self.bottom:
            print(f"Mixed: {self.top//self.bottom} {self.top%self.bottom}/{self.bottom}")
        else:
            print(f"Decimal: {self.top/self.bottom:.2f}")
    """
    2. Create a reduce function, that reduces rational numbers to their most basic equivalent form (e.g., 2/6 becomes 1/3). Modify your main function to demonstrate it.
    """
    def reduce(self):
        if self.top <= self.bottom:
            max_divisor = self.top
        else: 
            max_divisor = self.bottom
        
        for div in range(2, max_divisor + 1):
            while self.top % div == 0 and self.bottom % div == 0:
                self.top /= div
                self.bottom /= div
    """
    3. Write a multiply_by function that accepts another rational number and changes the value of the current object (multiply the two numerators to get the new numerator and the two denominators to get the new denominator). Modify your main function to demonstrate it.
    """
    def multiply_by(self, multTop, multBottom):
        self.top *= multTop
        self.bottom *= multBottom

def main():
    """
    This is the main driver for the program. It calls functions
    to prompt the user and get the results. Finally, it displays
    the results of the program.
    """
    # Core Requirements
    print("CORE REQUIREMENTS")
    number = Rational()
    print(f"Rational: {number.top}/{number.bottom}")

    number.prompt()
    print(f"Rational: {number.top}/{number.bottom}")

    number.display_decimal()

    print()
    # Stretch Challenges
    print("STRETCH CHALLENGES")
    number2 = RetionalStretch()
    print(f"Rational: {number2.top}/{number2.bottom}")

    number2.prompt()
    print(f"Rational: {number2.top}/{number2.bottom}")

    number2.display_decimal()

    number2.reduce()
    print(f"Rational: {number2.top}/{number2.bottom}")

    print("\nNew rational number for multiplication")
    multTop = int(input("Enter the numenator: "))
    multBottom = int(input("Enter the denominator: "))
    number2.multiply_by()
    print(f"Rational: {number2.top}/{number2.bottom}")

if __name__ == "__main__":
    main()