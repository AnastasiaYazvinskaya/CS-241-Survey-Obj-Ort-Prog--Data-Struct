"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Data Structure Homework 9
"""
import csv

def main():
    edu_levels_count = {}
    
    with open("census.csv") as csv_file:

        for row in csv_file:
            row = row.split(', ')
            
            if row[3] in edu_levels_count:
                edu_levels_count[row[3]] += 1
            else:
                edu_levels_count[row[3]] = 1

    for level in edu_levels_count:
        print(f"{edu_levels_count[level]} -- {level}")

if __name__ == "__main__":
    main()
