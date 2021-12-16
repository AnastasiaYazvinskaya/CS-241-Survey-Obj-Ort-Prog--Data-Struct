"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Checkpoint 4 (b)
"""
class Address:
    def __init__(self):
        self.street = input("Street: ")
        self.city = input("City: ")
        self.state = input("State: ")
        self.zip = input("Zip: ")

    def display(self):
        print(f"""{self.street}
{self.city}, {self.state} {self.zip}""")