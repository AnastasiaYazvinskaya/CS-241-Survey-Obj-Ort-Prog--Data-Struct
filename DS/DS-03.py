"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Data Structure Homework 3
"""
def main():
    odd = [] #нечетные
    even = [] #четные
    num = -1

    while (num != 0):
        num = int(input("Enter a number (0 to quit): "))

        if (num != 0):
            if (num%2 == 0):
                even.append(num)
            else:
                odd.append(num)

    print("\nEven numbers:")
    for number in even:
        print(number)

    print("\nOdd numbers:")
    for number in odd:
        print(number)

if __name__ == "__main__":
  main()
