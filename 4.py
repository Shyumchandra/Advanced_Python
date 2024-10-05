file=open("4.txt","r")

content=file.read()
print(content)
print()

line=file.readline()
print(line)
print()

lines=file.readlines()
for line in lines:
    print(line)
file.close()

file=open("4.txt","w")

file.write("Hello world\n")
file.writelines(["hey,beauty\n","hey,Ugly\n"])
file.close()

with open("4.txt","w") as file:
    file.write("Hello,World!")

from io import StringIO
text=StringIO("Hello,World!\n")
line=text.read()
print(line)