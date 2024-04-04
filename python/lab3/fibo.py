n=int(input("enter no. of terms: "))
i=0
a,b=0,1
c=0
print(f"{a},{b},",end="")
for i in range(1,n):
    a=b
    b=c
    c=a+b
    print(f"{c},",end="")

