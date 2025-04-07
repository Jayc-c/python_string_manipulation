# Prog02: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.

# Ask user to input a number (0 - 1000).
input_number = int(input("Enter a number (0 - 1000): "))

# Change user's input to string then add zeroes using zfill().
fixed_format = str(input_number).zfill(6)

# Print ouput numbers.
print(f"Fixed format : {fixed_format}")