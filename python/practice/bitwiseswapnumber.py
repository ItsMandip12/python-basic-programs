# Swap two numbers using bitwise XOR without functions
a = 5
b = 10

print(f"Before swapping: a = {a}, b = {b}")

# XOR the numbers to swap them
a = a ^ b
b = a ^ b
a = a ^ b

print(f"After swapping: a = {a}, b = {b}")
