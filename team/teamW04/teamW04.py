"""
Author: Anastasia Yazvinskaya, (Faud Torres), Lindsay Gardels, Christian Maciel
Class: CS 241 - 03 (Fall 2021)
Assignment: Team W04
"""

""" CORE REQUIREMENTS """
"""
1. Create a Date class in a file date.py with the above variables and methods.
"""
from date import Date, DateStretch
"""
2. Create an Assignment class in a file assignment.py with the above variables and methods. Have it import the Date class from the date.py file.
"""
from assignment import Assignment    
"""
3. Create a main function in a file main.py that creates a new Assignment, prompts for its values and display them. Have it import the Assignment class from the assignment.py file. Then, tar up your files and ensure that your solution passes testBed. (See the instructions for Check04B for more information.)
"""   
def main():
    """
    This is the main driver for the program. It calls functions
    to prompt the user and get the results. Finally, it displays
    the results of the program.
    """
    # Core Requirements
    task = Assignment()
    task.prompt()
    task.display()

    print()
    # Stretch Challenges
    task2 = Assignment()
    task2.start = DateStretch()
    task2.due = DateStretch()
    task2.end = DateStretch()
    task2.prompt()
    task2.display()
    task2.display_long()
    

if __name__ == "__main__":
    main()