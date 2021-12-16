"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Data Structure Homework 6
"""
from collections import deque

class Student:
    def __init__(self):
        self.name = ''
        self.course = ''

    def prompt(self):
        self.name = input("Enter name: ")
        self.course = input("Enter course: ")

    def display(self):
        print(f"Now helping {self.name} with {self.course}")

class HelpSystem:
    def __init__(self):
        self.waiting_list = deque([])

    def is_student_waiting(self):
        not_empty = False
        if len(self.waiting_list) != 0:
            not_empty = True

        return not_empty

    def add_to_waiting_list(self, student):
        student.prompt()
        self.waiting_list.append(student)

    def help_next_student(self):
        if self.is_student_waiting():
            self.waiting_list[0].display()
            self.waiting_list.popleft()
        else:
            print("No one to help")
        print()

def main():
    system = HelpSystem()
    cmd = 0

    while cmd != '3':
        print("""Options:
1. Add a new student
2. Help nex student
3. Quit""")
        cmd = input("Enter selection: ")
        print()

        if cmd == '1':
            system.add_to_waiting_list(Student())
        if cmd == '2':
            system.help_next_student()

    print("Goodbye")

if __name__ == "__main__":
    main()
