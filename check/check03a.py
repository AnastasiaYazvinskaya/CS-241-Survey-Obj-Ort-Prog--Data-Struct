"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Checkpoint 3 (a)
"""
class Student:
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

def prompt_student():
    student = Student(
        input("Please enter your first name: "),
        input("Please enter your last name: "),
        input("Please enter your id number: ")
        )
    return student

def display_student(student):
    print(f"""
Your information:
{student.id} - {student.first_name} {student.last_name}""")

def main():
    user = prompt_student()
    display_student(user)

if __name__ == "__main__":
  main()
