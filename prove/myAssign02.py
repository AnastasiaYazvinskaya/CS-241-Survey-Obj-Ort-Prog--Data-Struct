"""
Author: Anastasia Yazvinskaya
Class: CS 241 - 03 (Fall 2021)
Assignment: Prove 2
"""
#Function for computing the average comersial rate and return its value
def average_comm_rate(data_file, comm_rate_col):
  #preparing varibles for sum of rates and their amount
  sum = 0
  count = 0
  #going line by line
  for line in data_file:
    line = line.split(",")
    #increasing amount by 1 and adding rate to the sum
    count += 1
    sum += float(line[comm_rate_col])
  return (sum/count)

#Function for finding the highest rate and return the prepeared string for output
def highest_rate(data_file, comm_rate_col):
  #preparing the starting data for the line with lowest rate
  max = -1
  zip =""
  utility_name ="none"
  state =""
  #going line by line
  for line in data_file:
    line = line.split(",")
    #finding the highest rate and saving utility_name, zip and state for it
    if float(line[comm_rate_col]) > max:
      max = float(line[comm_rate_col])
      zip = line[0]
      utility_name = line[2]
      state = line[3]
  #creating the string for output
  highest_rate = utility_name+ " (" + zip + ", " + state + ") - $" + str(max)
  return highest_rate

#Function for finding the lowest rate and return the prepeared string for output
def lowest_rate(data_file, comm_rate_col):
  #preparing the starting data for the line with lowest rate
  min = 2
  zip =""
  utility_name ="none"
  state =""
  #going line by line
  for line in data_file:
    line = line.split(",")
    #finding the lowest rate and saving utility_name, zip and state for it
    if float(line[comm_rate_col]) < min:
      min = float(line[comm_rate_col])
      zip = line[0]
      utility_name = line[2]
      state = line[3]
  #creating the string for output
  lowest_rate = utility_name+ " (" + zip + ", " + state + ") - $" + str(min)
  return lowest_rate
    
#The main function for openning file, starting work with it and otput the neede data
def main():
  file_path = input("Please enter the data file: ")
  
  with open(file_path) as file:
    #Reading the first line
    aline = file.readline().split(",")
    #Finding the index of comm_rate collumn
    comm_rate_col = aline.index("comm_rate")
    #Saving dato from other lines into a variable
    data = file.readlines()
    #Printing with calling the function
    print(f"""
The average commercial rate is: {average_comm_rate(data, comm_rate_col)}

The highest rate is:
{highest_rate(data, comm_rate_col)}

The lowest rate is:
{lowest_rate(data, comm_rate_col)}""")
    
#Calling the main function
if __name__ == "__main__":
  main()