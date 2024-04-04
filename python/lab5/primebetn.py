l=15
m=25
count=0
while l<m:
    for i in range(2,l-1):
        if l%i==0:
                count=count+1
    if count==1:
         print(l+", ",end="")
    else:
         print("not")
    l=l+1
    
    