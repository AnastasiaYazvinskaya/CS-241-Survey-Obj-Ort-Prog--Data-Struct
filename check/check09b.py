"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Checkpoint 9 (b)
"""

def get_inverse(n):
    try:
        if n < 0:
            raise NegativeNumberError
        return(1/n)
    except ValueError:
        raise
    except ZeroDivisionError:
        raise
"""
    if not n.isnumeric():
        raise ValueError
    elif int(n) == 0:
        raise ZeroDivisionError
    elif int(n) < 0:
        raise NegativeNumberError()
    return (1/int(n))
"""
        

class NegativeNumberError(Exception):
    def __init__(self):
        super().__init__("Error: The value cannot be negative")
        

def main():
    try:
        num = int(input("Enter a number: "))
        inverse = get_inverse(num)
        print(f"The result is: {inverse}")
    except ValueError:
        print("Error: The value must be a number")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except NegativeNumberError as e:
        print(e)        

if __name__ == "__main__":
    main()
