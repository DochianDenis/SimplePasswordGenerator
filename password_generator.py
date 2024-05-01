import string
import random
import pyperclip

characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?/~"

passwordLength = int(input("The length of the password:"))
password = ''.join(random.choices(characters, k = passwordLength))

pyperclip.copy(password)
print(password)

