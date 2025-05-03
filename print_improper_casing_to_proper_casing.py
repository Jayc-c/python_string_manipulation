# Prog05: Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.

# Prompt user to input their full name.
full_name = input("Enter full name: ")

# Format the incorrect casing into proper casing.
fixed_case = full_name.title()

# Print formatted input.
print(f"Fixed casing: {fixed_case}")