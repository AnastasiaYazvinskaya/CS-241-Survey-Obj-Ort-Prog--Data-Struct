"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Prove 4
"""
class Product:
    def __init__(self, id="", name="", price=0, quantity=0):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return (self.price*self.quantity)

    def display(self):
        print(f"{self.name} ({self.quantity}) - ${self.get_total_price():.2f}")

#Product("1", "Pencil", 1.29, 10).display()