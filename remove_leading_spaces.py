# Prog01: Create a program that ask the user to input their fullname with several space characters at the beginning. 

# Ask user to input full name with spaces before the full name
full_name = input("Please input your full name with spaces in the beginning: ")

# Remove leading spaces using .lstrip()
full_name = full_name.lstrip()

# Print the input without the spaces in the beginning.