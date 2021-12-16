"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Prove 4
"""
from order import Order

class Customer:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.orders = []

    def get_order_count(self):
        return (len(self.orders))

    def get_total(self):
        sum = 0
        for order in self.orders:
            sum += order.get_total()
        return sum

    def add_order(self, order):
        self.orders.append(order)

    def display_summary(self):
        print(f"""Summary for customer '{self.id}':
Name: {self.name}
Orders: {self.get_order_count()}
Total: ${self.get_total():.2f}""")

    def display_receipts(self):
        print(f"""Detailed receipts for customer '{self.id}':
Name: {self.name}
""")
        for order in self.orders:
            order.display_receipt()
            if self.orders.index(order) != len(self.orders)-1:
              print()
