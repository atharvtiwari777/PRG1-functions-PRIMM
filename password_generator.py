import string
import random

def generate_password(length):
    if length < 8:
        print("Password length should be at least 8 characters.")
    
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    
    while not (any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
        password = ''.join(random.choice(chars) for _ in range(length))
    return password

print(generate_password(12))