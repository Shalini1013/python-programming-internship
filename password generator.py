import random

def password_generator(length=12, use_upper=True, use_numbers=True, use_special=True):
    # Basic character set (lowercase letters)
    characters = "abcdefghijklmnopqrstuvwxyz"

    # Add character options based on user preferences
    if use_upper:
        characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if use_numbers:
        characters += "0123456789"
    if use_special:
        characters += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    # Ensure there are characters to choose from
    if not characters:
        print("Error: No character sets selected!")
        return None

    # Generate a random password
    password = ''.join(random.choices(characters, k=length))
    return password

# User input for customization
try:
    length = int(input("Enter the desired password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    # Generate and display the password
    password = password_generator(length, use_upper, use_numbers, use_special)
    if password:
        print(f"Generated Password: {password}")
except ValueError:
    print("Invalid input! Please enter a valid number for the password length.")
