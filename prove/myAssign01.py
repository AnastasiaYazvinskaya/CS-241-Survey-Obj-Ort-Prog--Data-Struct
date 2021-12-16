"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Prove 1
"""
import random
from random import randint

seed_val = input("Welcome to the number guessing game!\nEnter random seed: ")
random.seed(seed_val)

attempt = 1
num = randint(1, 100)
restart = ""
  
while restart != "no":
  guess = int(input("\nPlease enter a guess: "))
  
  if guess == num:
    print(f"Congratulations. You guessed it!\nIt took you {attempt} guesses.")
    restart = input("\nWould you like to play again (yes/no)? ").lower()
    
    if restart == "yes":
      attempt = 1
      num = randint(1, 100)
    elif restart == "no":
      print("Thank you. Goodbye.")
    
    
  elif guess < num:
    print("Higher")
    attempt += 1
  elif guess > num:
    print("Lower")
    attempt += 1