file_name=input("Enter file name: ")
f=open(file_name,'r')
r=f.read()
f.close
file_name=input("Enter file name: ")
f=open(file_name,'w')
f.write(r)
f.close