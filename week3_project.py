import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

# Character pool
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
special_chars = string.punctuation

all_characters = lowercase + uppercase + digits + special_chars

# Ensure password contains at least one character from each category
password = [
    random.choice(lowercase),
    random.choice(uppercase),
    random.choice(digits),
    random.choice(special_chars)
]

# Fill remaining length
for i in range(length - 4):
    password.append(random.choice(all_characters))

# Shuffle password characters
random.shuffle(password)

# Convert list to string
final_password = "".join(password)

print("\nGenerated Secure Password:")
print(final_password)