try:
    num1=int(input("Enter 1st number"))
    num2=int(input("Enter 2nd number"))
    res=num1/num2
    print(res)
except ValueError:
    print("Please Enter Valid Numbers")
except ZeroDivisionError:
    print("cannot Divided by zero")
except(ValueError, ZeroDivisionError):
    print("check what you given")
else:
    print("Division Successful")
finally:
    print("Executed Successfully")
    
print()

age=int(input("age: "))
if age<0:
    raise ValueError("Age cannot be negative")

print()

class InvalidAgeError(Exception):
    def __init__(self,message="invalid age"):
        super().__init__(message)
def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age Cannot be Negative")
    if age > 120:
        raise InvalidAgeError("Age is Too High")
try:
    age=int(input("Age: "))
    check_age(age)
    print("correct age")
except InvalidAgeError as e:
    print(f"Error! {e}")
    