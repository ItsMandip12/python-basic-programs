n=int(input("Enter size of list"))
arr=[0]
i=0
while i >=n:
    val=input(f"enter {i+1}th value: ")
    arr.append(val)
    i=i+1
j=0
while j>=n:
    if arr[j+1]>arr[j]:
        arr[j]=arr[j+1]
    j=j+1

print(" Second largest element is: ",arr[2])