"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Checkpoint 10 (a)
"""
#Selecting Sort
def sort(numbers):
    """
    Fill in this method to sort the list of numbers
    """
    last_elm = len(numbers)-1          #8
    for i in range(len(numbers)-1, 0, -1):
        max_index = 0                  #0 (26)
        
        for j in range(1, last_elm+1, 1):
            if numbers[j] > numbers[max_index] :
                max_index = j          #2 (93)
                
        if last_elm != max_index:
            numbers[last_elm] += numbers[max_index]       #113 [88]
            numbers[max_index] = numbers[last_elm] - numbers[max_index]  #20 [44]
            numbers[last_elm] -= numbers[max_index]       #93 [44]

        last_elm -= 1                  #7
        
#Inserting Sort
def sort_2(numbers):

    for i in range(1, len(numbers), 1):
        position = i
        while numbers[position] < numbers[position-1] and position > 0:
            numbers[position] += numbers[position-1]
            numbers[position-1] = numbers[position] - numbers[position-1]
            numbers[position] -= numbers[position-1]
            
            position -= 1

#Bubble Sort
def sort_3(numbers):
    for pass_num in range(len(numbers)-1, 0, -1):
        for i in range(pass_num):
            if numbers[i] > numbers[i+1]:
                numbers[i] += numbers[i+1]
                numbers[i+1] = numbers[i] - numbers[i+1]
                numbers[i] -= numbers[i+1]
            

def prompt_for_numbers():
    """
    Prompts the user for a list of numbers and returns it.
    :return: The list of numbers.
    """

    numbers = []
    print("Enter a series of numbers, with -1 to quit")

    num = 0

    while num != -1:
        num = int(input())

        if num != -1:
            numbers.append(num)

    return numbers

def display(numbers):
    """
    Displays the numbers in the list
    """
    print("The list is:")
    for num in numbers:
        print(num)

def main():
    """
    Tests the sorting process
    """
    numbers = prompt_for_numbers()
    sort(numbers)
    display(numbers)

if __name__ == "__main__":
    main()