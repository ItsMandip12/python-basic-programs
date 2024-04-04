n=int(input("Enter upper limit "))
ecount=0
ocount=0
arr1={}
arr2={}
while n>=0:
    if n%2==0:
        print(f"{n} is even")
        
    else:
        ocount =ocount+1
        arr2=arr2.append(n)
    n=n-1

    