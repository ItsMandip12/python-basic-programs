file_name=input("Enter file name: ")
f=open(file_name,'w')
data=input("Enter contents to write")
f.write(data)
f.close