"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Checkpoint 4 (b)
"""
from credit_card import CreditCard

class Person:
    def __init__(self):
        self.name = input("Name: ")
        self.credit_card = CreditCard()

    def display(self):
        print(f"{self.name}")
        self.credit_card.display()

def main():
    Person().display()
    

if __name__ == "__main__":
  main()