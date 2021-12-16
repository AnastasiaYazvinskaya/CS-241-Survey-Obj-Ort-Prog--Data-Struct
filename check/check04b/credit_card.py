"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Checkpoint 4 (b)
"""
from address import Address

class CreditCard:
    def __init__(self):
        self.credit_card = input("Number: ")
        print("Mailing Address:")
        self.mailing_address = Address()
        print("Billing Address:")
        self.billing_address = Address()

    def display(self):
        print(f"""{self.credit_card}
Mailing Address:""")
        self.mailing_address.display()
        print("Billing Address:")
        self.billing_address.display()