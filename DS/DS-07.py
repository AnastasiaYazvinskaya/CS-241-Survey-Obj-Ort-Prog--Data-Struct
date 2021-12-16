"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Data Structure Homework 7
"""
def fib(n):                       #n = 3                   #n = 2
    num = 0                       #num = 0                 #
    if n < 2:                     #False                   #
        num = n
    elif n >= 2:                  #True                    #
        num = fib(n-1) + fib(n-2) #num = fib(2) + fib (1)  #num = fib(1) + fib(0)
    return(num)

def main():
    index = 0
    while index != -1:
        index = int(input("Enter a Fibnacci index: "))
        if index != -1:
            print(f"The Fibonacci number is: {fib(index)}")
            print()

if __name__ == "__main__":
    main()
