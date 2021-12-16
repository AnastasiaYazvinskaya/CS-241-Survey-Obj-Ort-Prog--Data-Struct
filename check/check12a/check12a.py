"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Checkpoint 12 (a)
"""
import pandas as pd

def main():
    census_data = pd.read_csv("census.csv", header=None)

    mean = census_data[0].mean()
    median = census_data[0].median()
    max = census_data[0].max()

    print(f"Mean age: {mean:.0f}")
    print(f"Median age: {median:.0f}")
    print(f"Max age: {max}")

if __name__ == "__main__":
    main()
