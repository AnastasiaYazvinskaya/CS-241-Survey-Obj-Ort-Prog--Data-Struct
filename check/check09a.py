"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Checkpoint 9 (a)
"""
def main():
    unvalid_input = True

    while unvalid_input:
        try:
            num = int(input("Enter a number: "))
            unvalid_input = False
            print(f"The result is: {num*2}")
        except ValueError:
            print("The value entered is not valid")
            

if __name__ == "__main__":
    main()