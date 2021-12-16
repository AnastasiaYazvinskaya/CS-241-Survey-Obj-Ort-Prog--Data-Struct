"""
Author: Anastasia Yazvinskaya, (Faud Torres), Lindsay Gardels, Christian Maciel
Class: CS 241 - 03 (Fall 2021)
Assignment: Team W04
"""

""" CORE REQUIREMENTS """
"""
1. Create the Point class as defined above. Then, create the Circle class as follows:
"""
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def prompt_for_point(self):
        self.x = int(input("Enter x: "))
        self.y = int(input("Enter y: "))

    def display(self):
        print(f"({self.x}, {self.y})")
"""
1-1. Create a Circle class that inherits from, or extends, the Point class.
"""
class Circle(Point):
    def __init__(self, radius=0):
        super().__init__()
        self.radius = radius
    """
    1-2. Create a blank method for prompt_for_circle and display.

    2. Implement the prompt_for_circle method. It should ask for a Circle as follows
    """
    def prompt_for_circle(self):
        self.prompt_for_point()
        self.radius = int(input("Enter radius: "))
    """
    3. Implement the display method. It should display a Circle as follows
    """
    def display(self):
        print("Center:")
        super().display()
        print(f"Radius: {self.radius}")

""" STRETCH CHALLENGES """
"""
1. Make a copy of your code from before, and start with the same Point class as before. This time your Circle should NOT inherit from Point, but rather should have a Point as a member variable called center.
"""
class CircleStretch():
    def __init__(self, center=Point(), radius=0):
        self.center = center
        self.radius = radius
    """
    2. Implement the prompt_for_circle and display methods for your Circle class as before.
    """
    def prompt_for_circle(self):
        self.center.prompt_for_point()
        self.radius = int(input("Enter radius: "))
    
    def display(self):
        print("Center:")
        self.center.display()
        print(f"Radius: {self.radius}")

    """
    3. Discuss with your team the pros and cons of the IS-A vs HAS-A approach to this problem. Determine which approach you feel is best and why. You'll provide your thoughts on this in your ponder submission for the week.
    """
    

def main():
    """
    This is the main driver for the program. It calls functions
    to prompt the user and get the results. Finally, it displays
    the results of the program.
    """
    # Core Requirements
    print("CORE REQUIREMENTS")
    obj = Circle()
    obj.prompt_for_circle()
    print()
    obj.display()

    print()
    # Stretch Challenges
    print("STRETCH CHALLENGES")
    obj = CircleStretch()
    obj.prompt_for_circle()
    print()
    obj.display()

if __name__ == "__main__":
    main()