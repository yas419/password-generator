import random
import string

print("Modules imported successfully!")
# Ask user how long they want the password
length = int(input("Enter the length of your password: "))
# Create a string of all possible characters
all_chars = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = "".join(random.choice(all_chars) for i in range(length))

# Show the password
print("Your generated password is:", password)
# Function to check password strength
def check_strength(password):
    length = len(password)
    lower = any(c.islower() for c in password)
    upper = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    symbol = any(c in string.punctuation for c in password)

    # Strength conditions
    if length >= 12 and lower and upper and digit and symbol:
        return "Strong"
    elif length >= 8 and ((lower and upper) or (digit and symbol)):
        return "Medium"
    else:
        return "Weak"

# Check and show strength
strength = check_strength(password)
print("Password Strength:", strength)
