import os
if os.path.exists("5.txt"):
    print("file exists")
else:
    os.mkdir("5.txt")
lists=os.listdir(".")
for line in lists:
    print(line)
    
os.mkdir("6.py")
os.rmdir("6.py")

if os.path.isfile("5.txt"):
    print("is file")
else:
    print("not a file")
    
if os.path.isdir("5.txt"):
    print("Is directory")
else:
    print("Not a Directory")

os.makedirs("6.py")
os.removedirs("6.py")

os.rename("5.txt","5.txt")
print()

