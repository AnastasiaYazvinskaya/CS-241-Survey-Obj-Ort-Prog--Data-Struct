"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Checkpoint 3 (b)
"""
class Complex:    
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.imaginary = imaginary

    def prompt(self):
        self.real = int(input("Please enter the real part: "))
        self.imaginary = int(input("Please enter the imaginary part: "))

    def display(self):
        print(f"{self.real} + {self.imaginary}i")


def main():
    c1 = Complex()
    c2 = Complex()

    print("The values are:")
    c1.display()
    c2.display()

    print()
    c1.prompt()

    print()
    c2.prompt()

    print("\nThe values are:")
    c1.display()
    c2.display()

if __name__ == "__main__":
    main()
