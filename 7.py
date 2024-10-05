import os

username = os.environ.get("USERNAME", "Unknown")
print(username)

value=os.getenv(username,default=None) 
print(value)
print()

os.environ[username]="babu"
value=os.getenv(username,None)
print(value)

print(os.name) 
print(os.getcwd())
print()

os.chdir("7")
print(os.getcwd())