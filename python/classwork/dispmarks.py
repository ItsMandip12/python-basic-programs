marks= [int(input(f"Enter marks for subject {i+1}: ")) for i in range(6)]

lowest_mark=min(marks)

print(f"The lowest marks is: {lowest_mark}")
