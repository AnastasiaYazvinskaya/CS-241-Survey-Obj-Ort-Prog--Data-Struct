"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Checkpoint 6 (b)
"""
class Phone:
    def __init__(self):
        self.area_code = 0
        self.prefix = 0
        self.suffix = 0

    def prompt_number(self):
        self.area_code = int(input("Area Code: "))
        self.prefix = int(input("Prefix: "))
        self.suffix = int(input("Suffix: "))

    def display_number(self):
        print(f"({self.area_code}){self.prefix}-{self.suffix}")

class SmartPhone(Phone):
    def __init__(self):
        super().__init__()

        self.email = ""

    def prompt(self):
        self.prompt_number()
        self.email = input("Email: ")

    def display(self):
        self.display_number()
        print(f"{self.email}")
    

def main():
    phone = Phone()
    print("Phone:")
    phone.prompt_number()
    print("\nPhone info:")
    phone.display_number()

    smartPhone = SmartPhone()
    print("\nSmart phone:")
    smartPhone.prompt()
    print("\nPhone info:")
    smartPhone.display()

if __name__ == "__main__":
    main()
