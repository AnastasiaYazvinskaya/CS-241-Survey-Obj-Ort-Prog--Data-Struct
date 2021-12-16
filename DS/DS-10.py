"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Data Structure Homework 10
"""
def main():
    numbers = [12, 18, 128, 48, 2348, 21, 18, 3, 2, 42, 96, 11, 42, 12, 18]
    #1
    numbers.insert(0, 5)
    print(numbers)
    #2
    numbers.remove(2348)
    print(numbers)
    #3
    new_numbers = [85, 93, 20, 4, 1946]
    numbers.extend(new_numbers)
    print(numbers)
    #4
    numbers.sort()
    print(numbers)
    #5
    numbers.reverse()
    print(numbers)
    #6
    print(numbers.count(12))
    #7
    print(numbers.index(96))
    #8
    middle = len(numbers)//2
    print(numbers[0:middle])
    print(numbers[middle+1:])
    #9
    print(numbers[::3])
    #10
    print(numbers[-5:])

if __name__ == "__main__":
    main()
