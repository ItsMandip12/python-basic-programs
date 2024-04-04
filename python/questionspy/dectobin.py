n=int(input("Enter number in decimal"))
a=[]
while n!=0:
    r=n%2
    a.append(r)
    n=n//2
a.reverse()
print(f"Number in binary is {a}")
 
