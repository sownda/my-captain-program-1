a=open("file.text","w+")
a.write("welcome all")
a.close()

b=open("file.text","r")
c=b.read(12)
print(c)

a=open("file.text","a")
s=input("enter a character")
a.write(s)
a.close
