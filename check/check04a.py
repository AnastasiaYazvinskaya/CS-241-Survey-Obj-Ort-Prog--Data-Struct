"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Checkpoint 4 (a)
"""
class Person:
    def __init__(self, name="anonymous", birth_year="unknown"):
        self.name = name
        self.birth_year = birth_year

    def display(self):
        print(f"{self.name} (b. {self.birth_year})")

class Book:
    def __init__(self, title="untitled", author=Person(), publisher="unpublished"):
        self.title = title
        self.author = author
        self.publisher = publisher

    def display(self):
        print(f"""{self.title}
Publisher:
{self.publisher}
Author:""")
        self.author.display()

def main():
    Book().display()
    print()
    
    print("Please enter the following:")
    name = input("Name: ")
    year = input("Year: ")
    title = input("Title: ")
    publisher = input("Publisher: ")
    print()
    
    Book(title, Person(name, year), publisher).display()

if __name__ == "__main__":
    main()
