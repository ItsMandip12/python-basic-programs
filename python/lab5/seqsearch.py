size=int(input("Enter size of array: "))
nums= [int(input(f"Enter element  {i+1}: ")) for i in range(size)]
req=int(input("Enter element to search: "))
i=0
for num in nums:
    i=i+1
    if num==req:
        print(f"Element position index is {i-1}")
    elif i==size:
        print("Element not found ")
    
    
    