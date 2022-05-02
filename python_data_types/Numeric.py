#Numeric type
print("----int_type-----------")
x=20
#display x;
print(x)
#display type of x
print(type(x))
print("/////////////////////////////////")
print("------float_type----------")
a=20.5
#display a
print(a)
#display type of a
print(type(a))
print("//////////////////////////////////")
print("-------complex_type-------------")
'''
A complex number has two parts, real part and imaginary part. Complex numbers are represented as A+Bi or A+Bj , where A is real part and B is imaginary part. Python supports complex data type as built-in feature which means we can directly perform different operations on complex number in python.
'''
p=20
r=5
q=complex(p,r)

print(q)
print(type(q))
g=5+9j
print(g.real)
print(g.imag)
print("-------Reading Complex Number From User------------------")
a=complex(input('enter complex number:'))
print('Given complex number is:',a)
print('-----------Finding Conjugate of Complex Number---------------')
a=10-6j
print(a.conjugate())
print('-------Addition, Subtraction, Multiplication & Division on Complex Number---------')
a=1+2j
b=3+4j
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("//////////////////////////////////////////////////////")
print('---Bool_type------------------------')
print(10>9)
print(10==9)
print(10<9)

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
