#prime number between 1 to 100
for n in range(1,100):
    count=0
    for i in range(2,n-1):
         if n%i==0:
               count=count+1
               break
    if(count==0):
         print(f"{n},",end="")