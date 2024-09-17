# Exploring Python's OS Module
# Objective: The goal of this assignment is to deepen your understanding of the OS module in Python.

# Task 1: Directory Inspector:

# Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. 
# Your script should prompt the user for the directory path and then display the contents.

# Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. 
# Handle exceptions for invalid paths or inaccessible directories.


import os

path = input("Enter a path to see the files and subdirectories: ")
try: 
    print(os.listdir(path))
except PermissionError:
    print("You don't have permission to access that file.")
except FileNotFoundError:
    print("That path was not found, please try again.")
except Exception as e:
    print(f"An error occurred: {e}")