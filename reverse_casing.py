# Prog06: Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.

# Ask the user to input their name in incorrect casing.
full_name = input("Input your full name in incorrect casing: ")

# Format the user's input into their reverse caising format.
reversed_casing = full_name.swapcase()

# Print the formatted output.
print(f"Reversed casing: {reversed_casing}")