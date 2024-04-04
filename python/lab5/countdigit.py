n=int(input("Enter a number: "))
count=0
r=n
while n!=0:
    count=count+1
    n=n//10

print(f"There are {count} digits present in given number")
