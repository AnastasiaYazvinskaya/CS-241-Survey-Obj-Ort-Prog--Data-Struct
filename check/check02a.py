"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Checkpoint 2 (a)
"""
def prompt_number():
  num = -1
  
  while num < 0:
    num = int(input("Enter a positive number: "))
    
    if num < 0:
      print("Invalid entry. The number must be positive.")
    else:
      print("")
      
  return num
  
def compute_sum(num_1, num_2, num_3):
  return (num_1 + num_2 + num_3)
  
def main():
  num_1 = prompt_number()
  num_2 = prompt_number()
  num_3 = prompt_number()
  
  sum = compute_sum(num_1, num_2, num_3)
  
  print(f"The sum is: {sum}")
  
if __name__ == "__main__":
  main()
