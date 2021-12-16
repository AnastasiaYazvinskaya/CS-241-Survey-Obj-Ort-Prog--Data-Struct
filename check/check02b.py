"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Checkpoint 2 (b)
"""
def main():
  file_path = input("Enter file: ")
  
  count_lines = 0
  count_words = 0
  
  with open(file_path) as file:
    for line in file:
      count_lines += 1
      
      words = line.split(" ")
      count_words += len(words)
      
  print(f"The file contains {count_lines} lines and {count_words} words.")
  
  
if __name__ == "__main__":
  main()
