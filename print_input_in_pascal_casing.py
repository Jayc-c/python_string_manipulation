# Prog09: Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

# Ask the user to input their full name in incorrect casing.
full_name = input("Enter your full name in incorrect casing: ")

# Convert to title case, remove spaces to make PascalCase.
pascal_case = full_name.title().replace(" ", "")

# Print the formatted output in pascal casing.