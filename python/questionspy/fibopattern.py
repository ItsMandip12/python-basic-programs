a,b=0,1
c=0
print(f"     {a}",end="")
for i in range(1, 6):
    l=0
    for j in range(i, 6):
        print(" ", end="")
    for k in range(1, i ):
        while l<=i:
            a=b
            b=c
            c=a+b
            print(f"{c} ", end="")
            l=l+1
    print("\n")