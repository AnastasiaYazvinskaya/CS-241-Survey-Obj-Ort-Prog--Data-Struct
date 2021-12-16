"""
Author: Anastasia Yazvinskaya, (Faud Torres), Lindsay Gardels, Christian Maciel
Class: CS 241 - 03 (Fall 2021)
Assignment: Team W04
"""

""" CORE REQUIREMENTS """
"""
1. Create a base class Employee, and two derived classes HourlyEmployee and SalaryEmployee, as follows:

1-1. Employee should have a string name and a display function that displays the name.
"""
class Employee:
    def __init__(self, name=""):
        self.name = name
    
    def display(self):
        print(f"{self.name}")
"""
1-2. HourlyEmployee should have an int hourly_wage and should override the display function to display the name and wage in the format: "John - $8/hour".
"""
class HourlyEmployee(Employee):
    def __init__(self, hourly_wage=0):
        super().__init__()
        self.hourly_wage = hourly_wage
    
    def display(self):
        print(f"{self.name} - ${self.hourly_wage}/hour")
"""
1-2. SalaryEmployee should have an int salary and should override the display function to display the name and salary in the format: "John - $50000/year".
"""
class SalaryEmployee(Employee):
    def __init__(self, salary=0):
        super().__init__()
        self.salary = salary
    
    def display(self):
        print(f"{self.name} - ${self.salary}/year")
"""
2. Create a main function that does the following:

    Declares a list for employees.

    Loops until the user enters "q" and prompts the user for an "h" (hourly employee) or an "s" (salary employee) or a "q" to quit.

    Then prompts for the name and the hourlyRate/salary.

    For each employee entered, creates a new employee of the correct type and adds it to the list.
"""
def main():
    """
    This is the main driver for the program. It calls functions
    to prompt the user and get the results. Finally, it displays
    the results of the program.
    """
    # Core Requirements
    print("CORE REQUIREMENTS")
    employees = []
    cmd = ""
    while cmd != "q":
        cmd = input("Hourly or Salary employee (h/s): ")
        if cmd == "h":
            employee = HourlyEmployee()
            employee.name = input("Enter name: ")
            employee.hourly_wage = int(input("Enter hourly wage: "))
            employees.append(employee)
        elif cmd == "s":
            employee = SalaryEmployee()
            employee.name = input("Enter name: ")
            employee.salary = int(input("Enter salary: "))
            employees.append(employee)
    """
    3. After the user enters "q", have main loop through the list and call the display method for each employee. Run your program and ensure that it looks correct.
    """
    print()
    for employee in employees:
        employee.display()

    print()
    # Stretch Challenges
    print("STRETCH CHALLENGES")
    # 2
    while cmd != "q":
        cmd = input("Hourly or Salary employee (h/s): ")
        if cmd == "h":
            employee = HourlyEmployeeStretch()
            employee.name = input("Enter name: ")
            employee.hourly_wage = int(input("Enter hourly wage: "))
            employee.hours = int(input("Enter hours: "))
            employees.append(employee)
        elif cmd == "s":
            employee = SalaryEmployeeStretch()
            employee.name = input("Enter name: ")
            employee.salary = int(input("Enter salary: "))
            employees.append(employee)
    print()
    for employee in employees:
        employee.display()
        print(f"Paycheck: {employee.get_paycheck()}")
        
        print()
        # 3
        display_employee_data(employee)

""" STRETCH CHALLENGES """
"""
1. Convert your Employee class to an abstract base class and the display function to be an abstract method.
"""
from abc import ABC
class EmployeeStretch(ABC):
    def __init__(self, name=""):
        self.name = name
    
    def display(self):
        print(f"{self.name}") 

    # 2
    def get_paycheck(self):
        pass
"""
2. Add to your HourlyEmployee a member variable for hours. Then, add an abstract method to the employee class for get_paycheck(), and override it in the derived classes. For hourly employees, this is calculated as the number of hours multiplied by the hourly rate. For salary employees, this should be the salary divided by 24.

    Change your code that prompts for the hourly employee to also prompt for the number of hours.

    In the loop in main that calls the display function, change it to also call the get_paycheck() function and display the pay check amount.
"""
class HourlyEmployeeStretch(EmployeeStretch):
    def __init__(self, hourly_wage=0, hours=0):
        super().__init__()
        self.hourly_wage = hourly_wage
        self.hours = hours
    
    def display(self):
        print(f"{self.name} - ${self.hourly_wage}/hour")

    def get_paycheck(self):
        return self.hourly_wage * self.hours

class SalaryEmployeeStretch(EmployeeStretch):
    def __init__(self, salary=0):
        super().__init__()
        self.salary = salary
    
    def display(self):
        print(f"{self.name} - ${self.salary}/year")

    def get_paycheck(self):
        return self.salary / 24
"""
3. Add a regular function (not a member function of any class), display_employee_data, that accepts an employee and calls its display function as well as its get_paycheck() function and displays the value. Then, remove this code from main, and replace it with a call to your new function.
"""
def display_employee_data(employee):
    employee.display()
    print(f"Paycheck: {employee.get_paycheck()}")

if __name__ == "__main__":
    main()