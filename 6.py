import os

path1="path/to/example.py"
path2="path/to/examples.py"
join=os.path.join(path1,path2)
print(join)
print()

directory,file=os.path.split(path1)
print(directory,file)
print()

print(os.path.dirname(path1))
print(os.path.basename(path1))
print()

print(os.path.abspath(path2))
print()

print(os.path.relpath(path2,start=None))