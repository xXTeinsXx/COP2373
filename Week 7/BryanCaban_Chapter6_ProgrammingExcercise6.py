# BryanCaban_Chapter6_ProgrammingExcercise6
# Validation of Phone Numbers, Social Security Numbers, and ZIP Codes

import re  # Importing the regular expressions module

# Function to validate phone numbers (Format: (XXX) XXX-XXXX)
def validate_phone_number(phone):
    pattern = r"^\(\d{3}\)\d{3}-\d{4}$"
    return bool(re.match(pattern, phone))

# Function to validate Social Security numbers (Format: XXX-XX-XXXX)
def validate_ssn(ssn):
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    return bool(re.match(pattern, ssn))

# Function to validate ZIP codes (Format: XXXXX or XXXXX-XXXX)
def validate_zip_code(zip_code):
    pattern = r"^\d{5}(-\d{4})?$"
    return bool(re.match(pattern, zip_code))

# Main function to get user input and validate it
def main():
    # Getting user input for phone number, SSN, and ZIP code
    phone = input("Enter a phone number (format: (XXX)XXX-XXXX): ")
    ssn = input("Enter a Social Security Number (format: XXX-XX-XXXX): ")
    zip_code = input("Enter a ZIP code (format: XXXXX or XXXXX-XXXX): ")

    # Checking if the phone number is valid
    if validate_phone_number(phone):
        print("✅ Valid phone number.")
    else:
        print("❌ Invalid phone number.")

    # Checking if the SSN is valid
    if validate_ssn(ssn):
        print("✅ Valid Social Security Number.")
    else:
        print("❌ Invalid Social Security Number.")

    # Checking if the ZIP code is valid
    if validate_zip_code(zip_code):
        print("✅ Valid ZIP code.")
    else:
        print("❌ Invalid ZIP code.")

# Asking the user if they want to run the validation
while True:
    runcode = input("\nWould you like to validate another set? (y/n): ").strip().lower()
    
    if runcode == 'y':  
        main()  # Run the main function again if user enters 'y'
    elif runcode == 'n':
        print("Goodbye! 👋")  # Exit the program gracefully
        break  # Break out of the loop
    else:
        print("Invalid input! Please enter 'y' to continue or 'n' to exit.")
