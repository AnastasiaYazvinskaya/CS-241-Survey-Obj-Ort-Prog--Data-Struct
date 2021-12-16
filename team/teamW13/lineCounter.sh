# !/bin/bash

# Author: Anastasia Yazvinskaya, Faud Torres, Lindsay Gardels, (Christian Maciel)
# Class: CS 241 - 03 (Fall 2021)
# Assignment: Team W13

# RUN the command below (without # sign) in the linux cmd for checking all steps
# ./lineCounter.sh /home/cs241 pyLines_1.txt pyLines_2.txt pyLines_3.txt py txt cpp

# CORE REQUIREMENTS
# 1 
# (./lineCounter.sh myFile.py - run Shell script which accepts a .py file as parameter)
# (./lineCounter.sh /home/cs241 - run Shell script which accepts a directory as parameter)
echo "Running on file: $1" # $1 - means first parameter (myFile.py or /home/cs241)

# 2 (./lineCounter.sh myFile.py)
#wc -l $1 # Uncomment this line for myFile.py

# 3 (./lineCounter.sh /home/cs241 py)
echo "Files in the directory:"

for file in $1/*.$5 #Find just .py files in /home/cs241 (fiths parameter in full file checking command)
do
  wc -l $file
done

# STRETCH CHALLENGES
# 1 (./lineCounter.sh /home/cs241 pyLines_1.txt py - run Shell script which accept a directory as first parameter and .txt file for outpyt as second parameter)
echo -n "" > $2 # Clean file for output (pyLine_1.txt)
for file in $1/*.$5 # Find just .py files in /home/cs241
do
  wc -l $file >> $2
done

# 2 (./lineCounter.sh /home/cs241 pyLines_1.txt pyLines_2.txt py - run Shell script which accept a directory as first parameter and .txt file for outpyt as second parameter)
echo -n "" > $3 # Clean file for output (pyLines_2.txt)
for file in $1/*/*.$5 # Find just .py files in sub-directories in /home/cs241
do
  wc -l $file >> $3
done

# 3 (./lineCounter.sh /home/cs241 pyLines_1.txt pyLines_2.txt pyLines_3.txt py txt cpp - run Shell script which accept a directory as first parameter and .txt file for outpyt as second parameter)
echo -n "" > $4 # Clean file for output (pyLines_3.txt)
for file in $(find $1/ -type f -name "*.$5" -o -name "*.$6" -o -name "*.$7") # Find .py, .txt, .cpp files in /home/cs241
do
  wc -l $file >> $4
done