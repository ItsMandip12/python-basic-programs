file_name=input("Enter file name: ")
f=open(file_name,'r')
print(len(f.readlines()))
f.close