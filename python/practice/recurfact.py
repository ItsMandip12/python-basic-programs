def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
    
n=int(input("Enter a number"))
print(f"The factorial of {n} is: {fact(n)}")