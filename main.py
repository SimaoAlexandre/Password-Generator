import random
import string

def generate_password(min_length, numbers = True, special_chars =True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    allowed_letters = letters
    if numbers:
        allowed_letters += digits
    if special_chars:
        allowed_letters += special
    pss = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pss) < min_length:
        char = random.choice(allowed_letters)
        pss += char
        if char in digits:
            has_number = True
        elif char in special:
            has_special = True

        meets_criteria = True

        if numbers:
            meets_criteria = has_number
        if special_chars:
            meets_criteria = meets_criteria and has_special

    return pss

min_length = int(input("Enter minimum length of password: "))
include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
include_special = input("Include special characters? (y/n): ").lower() == 'y'
password = generate_password(min_length, include_numbers, include_special)
print("Generated password:", password)