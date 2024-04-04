#input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#original values
print("Original values:")
print("First number:", num1)
print("Second number:", num2)


temp = num1
num1 = num2
num2 = temp

#swapped values
print("\nAfter swapping:")
print("First number:", num1)
print("Second number:", num2)
