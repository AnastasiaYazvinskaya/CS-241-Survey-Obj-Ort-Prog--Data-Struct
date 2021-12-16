"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Team W02
"""

""" CORE REQUIREMENTS """
"""
1. Create a function prompt_filename that prompts the user for 
a filename and returns it. Create a main function that calls the 
prompt_filename function, and displays the text, Opening file '...' 
replacing the "..." with the actual filename. Then, use the 
__name__ syntax to call the initial main function. Run your program 
and ensure that it words correctly.
"""
def prompt_filename():
    """
    Prompt the user for a filename and return it
    Returns:
        filename
    """
    filename = input("Enter the filename: ")
    return filename

"""
2. Create another function, parse_file that should receive a 
filename from main. It should then open the file and read through 
it line by line and word by word. For testing purposes, at this 
point print out each word in the file at this point.

3. Change your parse_file function so that it does not print 
anything out, but instead counts the number of times the word 
"pride" occurs. Have the function return this number and then 
change main to display this to the screen (e.g., "The word pride 
occurs xx times in this file").
"""
def parse_file(filename):
    """
    Parses a file and counts the occurrences of the word "pride"
    Args:
        filename: The file to be parsed
    Returns:
        count: The number of occurrences
    """
    count = 0
    with open(filename) as f:
        for line in f:
            words = line.split()
            for word in words:
                #print(word)
                if word == "pride":
                    count += 1
    return count

""" STRETCH CHALLENGES """
"""
1. Change your program so that it is case-insensitive. In other 
words, both "Pride" and "pride" should be counted.
"""
def parse_file_stretch1(filename):
    """
    Parses a file and counts the occurrences of the word "pride"
    Args:
        filename: The file to be parsed
    Returns:
        count: The number of occurrences
    """
    count = 0
    with open(filename) as f:
        for line in f:
            words = line.split()
            for word in words:
                if word.lower() == "pride":
                    count += 1
    return count

"""
2. Change your program so that it can count any word, not just 
"pride". Add a function to prompt the user for the word of their 
choice, then pass that word to the parse_file function and use it 
when displaying your results.
"""
def prompt_word():
    """
    Prompt the user for a word should be found and return it
    Returns:
        word
    """
    find_word = input("Enter the word: ")
    return find_word
def parse_file_stretch2(filename, find_word):
    """
    Parses a file and counts the occurrences of the word user chose
    Args:
        filename: The file to be parsed
        word: The word should be found
    Returns:
        count: The number of occurrences
    """
    count = 0
    with open(filename) as f:
        for line in f:
            words = line.split()
            for word in words:
                if word.lower() == find_word.lower():
                    count += 1
    return count

"""
3. Change your program so that it counts any words that contain the 
user's word as well. For example, if the user enters "pride" the 
words "pride" and "prideful" would both be counted.
"""
def parse_file_stretch3(filename, find_word):
    """
    Parses a file and counts the occurrences of the words that 
    contain the user's word 
    Args:
        filename: The file to be parsed
        word: The word should be found
    Returns:
        count: The number of occurrences
    """
    count = 0
    with open(filename) as f:
        for line in f:
            words = line.split()
            for word in words:
                if find_word.lower() in word.lower():
                    count += 1
    return count

def main():
    """
    This is the main driver for the program. It calls functions
    to prompt the user and get the results. Finally, it displays
    the results of the program.
    """
    filename = prompt_filename()
    print(f"Opening file '{filename}'")

    # Core Requirments
    print("CORE REQUIREMENTS")
    count = parse_file(filename)
    print(f"The word pride occurs {count} times in this file.")
    # Stretch Challenges
    print("STRETCH CHALLENGES")
    # 1
    count = parse_file_stretch1(filename)
    print(f"1. The word pride occurs {count} times in this file.")
    # 2
    word = prompt_word()
    count = parse_file_stretch2(filename, word)
    print(f"2. The word pride occurs {count} times in this file.")
    # 3
    word = prompt_word()
    count = parse_file_stretch3(filename, word)
    print(f"3. The word pride occurs {count} times in this file.")

if __name__ == "__main__":
    main()