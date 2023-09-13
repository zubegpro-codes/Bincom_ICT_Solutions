import random

# Generate a random 4-digit binary number
random_binary = ''.join(random.choice('01') for _ in range(4))

# Convert the binary number to decimal
decimal_number = int(random_binary, 2)

print(f"Random 4-digit binary number: {random_binary}")
print(f"Equivalent decimal number: {decimal_number}")