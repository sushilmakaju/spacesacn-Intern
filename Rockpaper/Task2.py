import random
import string

def random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = [] # creating empty list to add generated password
    for _ in range(length):
        random_char = random.choice(characters)
        password.append(random_char)
    return ''.join(password)

# Usage example
password = random_password()
print("Random Password:", password)
