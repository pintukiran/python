from cmath import e


a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
try:
    print(a/b)
except ValueError as e:
    print(e)

except Exception as e:
    print("plz enter valid  number",e)
finally:
    print("resource is closed")

