import string
import random
import pyperclip

# Define character sets
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"

# Combine all character sets
all_characters = lowercase_letters + uppercase_letters + digits + special_characters

# Generate a password of length (input from the user) using characters from the combined set
password_length = int(input("The length of the password:"))
password = ''.join(random.choices(all_characters, k = password_length))

# Saves the generated password to the clipboard.
pyperclip.copy(password)

print(password)
