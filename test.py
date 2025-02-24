import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special    

    pwd = []
    has_number = not numbers
    has_special = not special_characters

    while len(pwd) < min_length or not (has_number and has_special):
        new_char = random.choice(characters)
        pwd.append(new_char)

        if new_char in digits:
            has_number = True
        if new_char in special:
            has_special = True

    random.shuffle(pwd)  # Ensures randomness in character order
    return "".join(pwd)

# User input
min_length = int(input("Enter the minimum length: "))
has_numbers = input("Do you want to have numbers (y/n)? ").strip().lower() == "y"
has_special = input("Do you want to have special characters (y/n)? ").strip().lower() == "y"

# Generate and display the password
pwd = generate_password(min_length, has_numbers, has_special)
print("Generated Password:", pwd)
