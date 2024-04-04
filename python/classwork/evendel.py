numbers= [int(input(f"Enter 10 numbers  {i+1}: ")) for i in range(10)]
j=9
i=0
while i<=j:
    if numbers[i] % 2==0:
        print(f"{numbers[i]} is deleted")
        numbers.remove(numbers[i])
    i=i+1
print(numbers)